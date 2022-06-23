#import everything needed to access sqlite databases
import sqlite3
from variables import db_path,items
import re
tags=['fantasy','sf','martial arts','comedy']
#open database using sqlite3
query='select'
print(db_path)

sqliteConnection = sqlite3.connect(db_path)
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")

sqlite_select_Query = "select sqlite_version();"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()
print("SQLite Database Version is: ", record)
#query2='select * from tags'
#sqlite_select_Query = query2
#cursor.execute(sqlite_select_Query)
#record = cursor.fetchall()
#last_id=len(record)
x=1
'''for row in tags:
    id=last_id
    adding_id=id+x
    command="INSERT INTO tags (id,name) VALUES (?, ?)"
    values=(adding_id,row)
    #cmd=command + ' ' + values

    cursor.execute(command,values)
    sqliteConnection.commit()
    x+=1
    #print(values)
    #print(adding_id,' ', row)'''
ids=[2,4,5,6] 
tag=[10,11,12]
query3='select * from books_tags_link'
sqlite_select_Query=query3
cursor.execute(sqlite_select_Query)
record=cursor.fetchall()
lastid=len(record)
y=1
for item in ids: #this segment adds the provided data into the database
    for t in tag:
        id=lastid
        add_id=id+y
        command="INSERT INTO books_tags_link(id,book,tag) VALUES(?,?,?)"
        values=(add_id,item,t)
        cursor.execute(command,values)
        sqliteConnection.commit()
        y+=1
        #print(values)
    #print("result is: ", record)
cursor.execute(sqlite_select_Query)
record=cursor.fetchall()
print(record)
cursor.close()

