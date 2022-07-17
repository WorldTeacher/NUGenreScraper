from bs4 import BeautifulSoup
import sqlite3
from variables import Calibre_Database_Path
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from lxml import html
from googlesearch import search
import time
import glob
import pandas as pd
import os

#access database
sqliteConnection = sqlite3.connect(Calibre_Database_Path)
cursor = sqliteConnection.cursor()
print("Database successfully Connected to SQLite")
print("now searching for the series names")
#get all series names
series_datadict_bookid={'id':[],'name':[],'book_ids':[]}
complete_series_list=[]
series_datadict={'id':[],'name':[],'book_ids':[]}
series_data=[]
#select last id from series
#cursor.execute("SELECT id FROM series")
#record = cursor.fetchall()
cursor.execute("SELECT id,name FROM series")
results=cursor.fetchall()

for result in results:
    series_datadict['id']=result[0]
    series_datadict['name']=result[1]
    series_data.append(series_datadict.copy())

#using the dict, go to book_series_link and get the books linked to the series
for series in series_data:
    id=series['id']
    name=series['name']
    #id=series['id']
    cursor.execute("SELECT book FROM books_series_link WHERE series=?",(id,))
    record = cursor.fetchall()
    
    series_datadict_bookid['id']=id
    series_datadict_bookid['name']=name
    book_ids=[]
    for row in record:
        book_ids.append(row[0])
    series_datadict_bookid['book_ids']=book_ids
    complete_series_list.append(series_datadict_bookid.copy())
print(complete_series_list)
#write to csv
df=pd.DataFrame(complete_series_list)
df.to_csv('series_list.csv',sep=',')
print("series_list.csv written")
cursor.close()


