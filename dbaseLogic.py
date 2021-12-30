import sqlite3
# creates a SQLite cursor automatically
connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row  # gets named access to data, dict like


def createTable():
    with connection:
        connection.execute(
            "create table if not exists entries (content TEXT, date TEXT);"
        )


def addEntry(entry_content, entry_date):
    with connection:
        # doing this as it's done below protects from sql injection attacks
        connection.execute(
            "insert into entries values(?, ?);", (entry_content, entry_date)
        )
    print("Entry added.")


def getEntries():
    cursor = connection.execute("select * from entries;")
    return cursor
