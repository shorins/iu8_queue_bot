import sqlite3
import os

DB_PATH = 'src/queue_bot.db'
INIT_SCRIPT = 'src/db/init_db.sql'

def verify_schema():
    # Remove existing DB to force recreation
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing DB: {DB_PATH}")

    # Initialize DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    with open(INIT_SCRIPT, 'r') as f:
        sql_script = f.read()
    
    cursor.executescript(sql_script)
    conn.commit()
    print("Database initialized.")

    # Check chat table schema
    cursor.execute("PRAGMA table_info(chat)")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    
    print(f"Columns in 'chat' table: {column_names}")
    
    if 'assignee_id' not in column_names:
        print("SUCCESS: 'assignee_id' column is NOT present in 'chat' table.")
    else:
        print("FAILURE: 'assignee_id' column IS present in 'chat' table.")
        exit(1)

    if 'chat_id' in column_names and 'chat_title' in column_names:
        print("SUCCESS: 'chat_id' and 'chat_title' columns are present.")
    else:
        print("FAILURE: Missing required columns.")
        exit(1)

    conn.close()

if __name__ == '__main__':
    verify_schema()
