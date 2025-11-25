from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from db.sqlite_db import sql_add_user

class UserTrackingMiddleware(BaseMiddleware):
    async def on_process_update(self, update: types.Update, _):
        user = None
        if update.message:
            user = update.message.from_user
        elif update.callback_query:
            user = update.callback_query.from_user
        elif update.inline_query:
            user = update.inline_query.from_user
        elif update.chosen_inline_result:
            user = update.chosen_inline_result.from_user
        elif update.my_chat_member:
            user = update.my_chat_member.from_user
        elif update.chat_member:
            user = update.chat_member.from_user
        
        if user and not user.is_bot:
            await sql_add_user(
                user.id, 
                user.username, 
                user.first_name, 
                user.last_name
            )
