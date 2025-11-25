from aiogram import types, Dispatcher

from create_bot import dp, bot
from db.sqlite_db import sql_add_admin, sql_add_managed_chat, sql_delete_managed_chat


async def new_chat_handler(message: types.Message):
    # Check that bot has been added to chat.
    if any(bot.id == member.id for member in message.new_chat_members):
        user = message.from_user
        await sql_add_admin(user.id, user.username)
        await sql_add_managed_chat(message.chat.id, message.chat.title)
        await message.reply(f"Привет! Я бот для очередей.\n"
                            "Теперь любой участник может создать очередь прямо здесь.\n"
                            "Просто напишите /create_queue или /plan_queue.")


async def left_chat_handler(message: types.Message):
    # Check that bot has been deleted from chat.
    if bot.id == message.left_chat_member.id:
        await sql_delete_managed_chat(message.chat.id)


def register_shared_handlers(dp_: Dispatcher) -> None:
    """
    Function for registration all handlers for everyone.
    """
    # dp.register_message_handler(echo, state=None)
    dp_.register_message_handler(new_chat_handler, content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
    dp_.register_message_handler(left_chat_handler, content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
