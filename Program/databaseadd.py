#import everything needed to access sqlite databases
from bs4 import BeautifulSoup
import sqlite3
from variables import test_db
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from lxml import html
from googlesearch import search
import time
import glob
import pandas as pd
import os

genre_url="https://www.novelupdates.com/genre-explanation/"
genre_location={"class":"w-blog-content"}

tag_url="https://www.novelupdates.com/list-tags/?st=1&pg="
tag_location={"class":"g-cols wpb_row offset_default staglistall"}
tag_page_count=16
url=tag_url
#connect to the database and get current amount of genres
sqliteConnection = sqlite3.connect(test_db)
genrecount=0
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")
cursor.execute("SELECT COUNT(*) FROM tags")
record = cursor.fetchall()
for row in record:
    genrecount=row[0]

print("Current amount of genres in the database: ", genrecount)
cursor.close()
print("Database connection is closed")
#check if genre.csv and tags.csv exist
if os.path.exists('/home/alexander/GitHub/NUGenreScraper/genres.csv') and os.path.exists('/home/alexander/GitHub/NUGenreScraper/tags.csv'):
    print("genre.csv and tags.csv exist")
else:
    
    print("genre.csv and tags.csv do not exist")
    genredict={'id':[],'name':[]}
    genrelist=[]
    genreid=genrecount+1
    taglist=[]
    #get all genres to list
    openurl=Request(genre_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage=urlopen(openurl).read()

    soup=BeautifulSoup(webpage, 'lxml')
    #print(soup.prettify())
    test=soup.find_all("div",genre_location)
    genres=soup.find_all("b",{'class':'genreexplain'})

    #in genres find the value after a href in > </a>
    for genre in genres:
        #print(genre.text)
        genredict['name'].append(genre.text)
        genredict['id'].append(genreid)
        genrelist.append(genredict.copy())
        genreid+=1

    p=1
    while p != tag_page_count+1:
        url=tag_url+str(p)
        print(url)
        openurl=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage=urlopen(openurl).read()
        soup=BeautifulSoup(webpage, 'lxml')
        #find the list entries in the page
        tag_half=soup.find_all("div","one-half")
        for tagentry in tag_half:
            tag=tagentry.find_all("a")
            for tag in tag:
                taglist.append(tag.text)
        p+=1    

    #make a csv for the genres
    df=pd.DataFrame(genredict)
    df.to_csv('genres.csv',index=False)

    #make a csv for the tags id;tag
    df=pd.DataFrame(taglist)
    df.to_csv('tags.csv',sep=',')
    print("genre.csv and tags.csv created")

#open the csv files
csv_genres=pd.read_csv('genres.csv')
csv_tags=pd.read_csv('tags.csv')
#open the database and write the genres into it
sqliteConnection = sqlite3.connect(test_db)
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")
#check if the genres are already in the database
for genre in csv_genres['name']:
    cursor.execute("SELECT COUNT(*) FROM tags WHERE name=?",(genre,))
    record = cursor.fetchall()
    for row in record:
        if row[0]==0:
            cursor.execute("INSERT INTO tags (name) VALUES (?)",(genre,))
            sqliteConnection.commit()
            print("Genre added: ",genre)
        else:
            print("Genre already in database: ",genre)
cursor.close()
print("Database connection is closed")
#find tag id for each tag in the csv
for tag in csv_tags['0']:
    cursor.execute("SELECT COUNT(*) FROM  custom_column_21 WHERE name=?",(tag,))
    record = cursor.fetchall()
    for row in record:
        if row[0]==0:
            cursor.execute("INSERT INTO  custom_column_21 (name) VALUES (?)",(tag,))
            sqliteConnection.commit()
            print("Genre added: ",tag)
        else:
            print("Genre already in database: ",tag)
'''
query='select'
print(test_db)

sqliteConnection = sqlite3.connect(test_db)
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
for row in tags:
    id=last_id
    adding_id=id+x
    command="INSERT INTO tags (id,name) VALUES (?, ?)"
    values=(adding_id,row)
    #cmd=command + ' ' + values

    cursor.execute(command,values)
    sqliteConnection.commit()
    x+=1
    #print(values)
    #print(adding_id,' ', row)
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
'''
