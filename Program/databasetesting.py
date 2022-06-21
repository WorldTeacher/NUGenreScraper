#import everything needed to access sqlite databases
import sqlite3
from variables import db_path,items
import re

#open database using sqlite3

print(db_path)

sqliteConnection = sqlite3.connect(db_path)
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")

sqlite_select_Query = "select sqlite_version();"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()
print("SQLite Database Version is: ", record)
cursor.close()

