import os
import sqlite3
from datetime import datetime, timedelta
from typing import Tuple

conn = None
cursor = None

def init_connection():
    global conn, cursor
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # src
    db_path = os.path.join(base_dir, 'db_data', 'queue_bot.db')
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

init_connection()


def start_db() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sql_file_path = os.path.join(base_dir, 'init_db.sql')

    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)
    conn.commit()

    # Migration for message_thread_id
    try:
        cursor.execute("ALTER TABLE queues_list ADD COLUMN message_thread_id INTEGER DEFAULT NULL")
        conn.commit()
        print("Added message_thread_id column to queues_list")
    except sqlite3.OperationalError:
        # Column likely already exists
        pass

    if conn:
        print("Data base has been connected!")


def sql_get_queue_list(admin_id_: int) -> list:
    cursor.execute(
        "SELECT id, queue_name, start, chat_id, chat_title  FROM queues_list WHERE assignee_id = ?",
        (admin_id_,)
    )

    return cursor.fetchall()


async def sql_get_queue_from_list(id_: int) -> tuple:
    cursor.execute(
        "SELECT *  FROM queues_list WHERE id = ?",
        (id_,)
    )

    return cursor.fetchone()


def sql_get_chat_title(chat_id_: int) -> tuple:
    cursor.execute(
        "SELECT chat_title FROM chat WHERE chat_id = ?", (chat_id_,)
    )

    return cursor.fetchone()





async def sql_add_admin(admin_id_: int, user_name_: str) -> None:
    cursor.execute(
        "INSERT OR IGNORE INTO admin VALUES (?, ?)",
        (admin_id_, user_name_)
    )
    conn.commit()


async def sql_add_managed_chat(chat_id_: int, chat_title_: str) -> None:
    cursor.execute(
        "INSERT INTO chat ('chat_id', 'chat_title') VALUES (?, ?)",
        (chat_id_, chat_title_)
    )
    conn.commit()


async def sql_delete_managed_chat(chat_id_: int) -> None:
    cursor.execute(
        "DELETE FROM chat WHERE chat_id = ?", (chat_id_,)
    )
    conn.commit()
    cursor.execute(
        "DELETE FROM queues_list WHERE chat_id = ?", (chat_id_,)
    )
    conn.commit()


async def sql_add_queue(admin_id_: int, queue_name_: str, start_dt: datetime, chat_id_: int, chat_title_: str, message_thread_id_: int = None) -> tuple:
    cursor.execute(
        "INSERT INTO queues_list ('assignee_id', 'queue_name', 'start', 'chat_id', 'chat_title', 'message_thread_id') "
        "VALUES (?, ?, ?, ?, ?, ?)", (admin_id_, queue_name_, start_dt, chat_id_, chat_title_, message_thread_id_)
    )
    conn.commit()

    cursor.execute(
        "SELECT id FROM queues_list WHERE assignee_id = ? AND queue_name = ? AND chat_id = ?",
        (admin_id_, queue_name_, chat_id_)
    )

    return cursor.fetchone()


async def sql_delete_queue(id_: int) -> Tuple[int, int]:
    cursor.execute(
        "SELECT chat_id FROM queues_list WHERE id = ?", (id_,)
    )
    chat_id: tuple = cursor.fetchone()

    cursor.execute(
        "DELETE FROM queues_list WHERE id = ?", (id_,)
    )
    conn.commit()

    cursor.execute(
        "SELECT msg_id FROM queue WHERE id = ?", (id_,)
    )
    msg_id: tuple = cursor.fetchone()

    cursor.execute(
        "DELETE FROM queue WHERE id = ?", (id_,)
    )
    conn.commit()

    return chat_id[0], msg_id[0]


async def sql_post_queue_msg_id(queue_id_: int, msg_id_: int):
    cursor.execute(
        "INSERT INTO queue ('id', 'msg_id') VALUES (?, ?)", (queue_id_, msg_id_)
    )
    conn.commit()


async def sql_add_user(user_id: int, username: str, first_name: str, last_name: str) -> None:
    now = datetime.now()
    cursor.execute(
        "INSERT INTO users (user_id, username, first_name, last_name, first_seen, last_seen) "
        "VALUES (?, ?, ?, ?, ?, ?) "
        "ON CONFLICT(user_id) DO UPDATE SET "
        "username=excluded.username, "
        "first_name=excluded.first_name, "
        "last_name=excluded.last_name, "
        "last_seen=excluded.last_seen",
        (user_id, username, first_name, last_name, now, now)
    )
    conn.commit()


async def sql_get_users_count() -> int:
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]


async def sql_get_active_users_count(days: int) -> int:
    limit_date = datetime.now() - timedelta(days=days)
    cursor.execute("SELECT COUNT(*) FROM users WHERE last_seen >= ?", (limit_date,))
    return cursor.fetchone()[0]
