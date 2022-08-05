import sqlite3
from variables import Calibre_Database_Path
import pandas as pd
from urllib.request import urlopen, Request
import re
from bs4 import BeautifulSoup
import time
import logger
import os
import sys
#from 

url="https://www.novelupdates.com/genre-explanation/"
'''req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())
#find genreexplain in the html
for link in soup.find_all('a'):
    pass'''
genredict={'id':[],'name':[]}
genrecount=0
genreid=genrecount+1
#get all genres to list
openurl=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage=urlopen(openurl).read()
soup=BeautifulSoup(webpage, 'html.parser')
genres=soup.find_all("b",{'class':'genreexplain'})
for genre in genres:
    print(genre.text)
    genredict['name'].append(genre.text)
    genredict['id'].append(genreid)
    genreid+=1