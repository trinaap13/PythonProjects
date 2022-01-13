# A file for helper functions to avoid repeating logic

import sqlite3

DB_PATH = './todo.db' # Update accordingly
NOTSTARTED = 'Not started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'


def add_to_list(item):
    try:
        # Establishing connection to the db
        conn = sqlite3.connect(DB_PATH)

        # Once connected, use the cursor object to execute queries
        c = conn.cursor()

        # Keep initial status as Not Started
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))

        # Commit to save the change
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None
