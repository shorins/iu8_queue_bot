from datetime import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup

from create_bot import dp, bot
from db.sqlite_db import sql_get_queue_list, sql_add_queue, sql_add_admin, \
    sql_delete_queue, sql_get_chat_title
from keyboards import admin_kb
from keyboards.client_kb import PLAN_QUEUE_TEXT, DELETE_QUEUE_TEXT, PLANNED_QUEUES_TEXT
from services.admin_service import wait_for_queue_launch


class FSMPlanning(StatesGroup):
    choose_chat = State()
    queue_name = State()
    queue_name = State()


class FSMDeletion(StatesGroup):
    queue_choice = State()


async def cancel_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.delete()
    await callback.answer('🚫 Действие отменено')
    await state.finish()


async def queues_list_handler(msg: types.Message) -> tuple:
    found_queues = sql_get_queue_list(msg.from_user.id)
    if not found_queues:
        await msg.reply(
            "🙊 У вас пока нет запланированных очередей.\nЗапланируем одну?",
            reply_markup=admin_kb.inl_plan_kb
        )
        return found_queues, None

    out_str = str()
    for _, queue_name, dt, _, chat_title in found_queues:
        out_str += f"📌«{queue_name}» в чате «{chat_title}» " \
                   f"{datetime.strptime(dt, '%Y-%m-%d %H:%M:%S%z').strftime('%d.%m.%Y в %H:%M')}\n"

    planned_msg = await msg.reply(f"⤵️ Вот запланированные вами очереди:\n{out_str}")

    return found_queues, planned_msg


""" Planning queue zone"""


async def start_planning(msg: types.Message, state: FSMContext) -> None:
    if msg.chat.type == types.ChatType.PRIVATE:
        await msg.reply("⚠️ Создание очередей теперь доступно только в групповых чатах.\n"
                        "Перейдите в группу и отправьте /create_queue или /plan_queue.")
        return

    # In group chat, start immediately
    await FSMPlanning.queue_name.set()
    async with state.proxy() as data:
        data['chat_id'] = msg.chat.id
        data['chat_title'] = msg.chat.title

    await msg.reply("📝 Введите название новой очереди:",
                    reply_markup=admin_kb.inl_cancel_kb)


async def queue_plan_handler(msg: types.Message, state: FSMContext) -> None:
    await start_planning(msg, state)


# Removed queue_plan_inline_handler and queue_set_chat_handler as they are no longer needed



async def set_queue_name_handler(msg: types.Message, state: FSMContext) -> None:
    if not msg.text or msg.text in (PLAN_QUEUE_TEXT, DELETE_QUEUE_TEXT, PLANNED_QUEUES_TEXT):
        await bot.send_message(
            msg.from_user.id, '❌ Кажется, вы ничего не написали! Задайте название очереди',
            reply_markup=admin_kb.inl_cancel_kb
        )
        return
    async with state.proxy() as data:
        data['queue_name'] = msg.text
    # Immediate start
    start_datetime = datetime.now()
    
    # Add to DB
    chat_id, chat_title = data['chat_id'], data['chat_title']
    queue_id = await sql_add_queue(msg.from_user.id, msg.text, start_datetime, chat_id, chat_title)

    await msg.reply(
        f"✅Очередь «{msg.text}» создана и запущена!\n"
        f"Начало: {start_datetime.strftime('%d.%m.%Y в %H:%M')}"
    )

    await state.finish()
    await wait_for_queue_launch(start_datetime, chat_id, queue_id[0])


""" Deleting queue zone"""


async def choose_queue_to_delete_handler(msg: types.Message) -> None:
    planned_queues, del_msg = await queues_list_handler(msg)

    if not planned_queues or del_msg is None:
        return

    inl_kb_choices = InlineKeyboardMarkup()
    for queue_id, queue_name, _, _, _ in planned_queues:
        inl_kb_choices.add(types.InlineKeyboardButton(
            text=queue_name, callback_data=f"delete_queue_{queue_id}")
        )
    inl_kb_choices.add(admin_kb.cancel_button)

    global messages_tuple
    messages_tuple = (del_msg, await msg.reply('🗑 Выберите очередь, которую хотите удалить:',
                                                      reply_markup=inl_kb_choices))

    await FSMDeletion.queue_choice.set()


async def delete_queue_handler(callback: types.CallbackQuery, state: FSMContext):
    chat_id, msg_id = await sql_delete_queue(int(callback.data[len("delete_queue_"):]))
    await bot.delete_message(chat_id, msg_id)
    await callback.answer('💥 Очередь удалена')
    await messages_tuple[0].delete()
    await messages_tuple[1].delete()
    await state.finish()


def register_admin_handlers(dp_: Dispatcher) -> None:
    """
    Function for registration all handlers for admin.
    :return: None
    """
    dp_.register_callback_query_handler(
        cancel_handler, text="cancel_call", state="*"
    )
    dp_.register_message_handler(
        queues_list_handler, Text(equals='🗒 Список запланированных очередей'), state=None
    )
    dp_.register_message_handler(
        queues_list_handler, commands="queues_list", state=None
    )
    # Plan queue.
    dp_.register_message_handler(
        queue_plan_handler, Text(equals='📌 Запланировать очередь'), state=None
    )
    dp_.register_message_handler(
        queue_plan_handler, commands=['plan_queue', 'create_queue'], state=None
    )
    dp_.register_message_handler(
        set_queue_name_handler, content_types='text', state=FSMPlanning.queue_name
    )
    # Delete queue.
    dp_.register_message_handler(
        choose_queue_to_delete_handler, Text(equals='🗑 Удалить очередь'), state=None
    )
    dp_.register_message_handler(
        choose_queue_to_delete_handler, Text(equals='🗑 Удалить очередь'), commands='delete_queue', state=None
    )
    dp_.register_callback_query_handler(
        delete_queue_handler, Text(startswith='delete_queue_'), state=FSMDeletion.queue_choice
    )
