import sqlite3
from variables import Calibre_Database_Path
import pandas as pd
from urllib.request import urlopen, Request
import re
from bs4 import BeautifulSoup
import time
import logger
'''
This is the database control script for the NUGenreScraper program.
It is used to connect to the database, and to add new content, such as genres and Tags to the database.
TODO: add comments describing what each function does
TODO: clean up the code
TODO: add logging

'''
#database=Calibre_Database_Path
log=logger.log()

class db:   #class for database connection
  
    def __init__(self):
        log.info("Logging started")
        log.debug("Connecting to database")
        msg=str("Connecting to database: "+Calibre_Database_Path)
        log.debug(msg)
        database=Calibre_Database_Path
        self.db=sqlite3.connect(database)
        self.cursor=self.db.cursor()
        self.genrecount=0
        self.genre={'genre_url':"https://www.novelupdates.com/genre-explanation/",'genre_location':{"class":"w-blog-content"}}
        self.tag={'tag_url':"https://www.novelupdates.com/list-tags/?st=1&pg=",'tag_location':{"class":"g-cols wpb_row offset_default staglistall"}}

    def db_version(self):   #get the version of the database
        log.info("Getting version of database")
        cursor = self.cursor
        query="select sqlite_version()"
        cursor.execute(query)
        record = cursor.fetchall()
        
        record=str(record)
        record=record.replace("(","")
        record=record.replace(")","")
        record=record.replace("'","")
        record=record.replace(",","")
        log_message="SQLite Database Version is: "+str(record)
        log.info(log_message)
        log.debug("Database closed after getting version")

    def db_get_series(self):    #get all series from the database
        log.info("Getting all series from database")
        cursor = self.cursor
        series_datadict_bookid={'id':[],'name':[],'book_ids':[]}
        complete_series_list=[]
        series_datadict={'id':[],'name':[],'book_ids':[]}
        series_data=[]
        cursor.execute("SELECT id,name FROM series")
        results=cursor.fetchall()

        for result in results:
            log_message="Adding Series ID: "+str(result[0])+" Series Name: "+str(result[1]+ "to list")
            log.debug(log_message)
            series_datadict['id']=result[0]
            series_datadict['name']=result[1]
            series_data.append(series_datadict.copy())

        #using the dict, go to book_series_link and get the books linked to the series
        log.info("Getting all books linked to series")
        for series in series_data:
            id=series['id']
            name=series['name']
            msg="Getting books linked to series: "+str(name)
            log.debug(msg)
            
            cursor.execute("SELECT book FROM books_series_link WHERE series=?",(id,))
            record = cursor.fetchall()
            
            series_datadict_bookid['id']=id
            series_datadict_bookid['name']=name
            book_ids=[]
            for row in record:
                book_ids.append(row[0])
            series_datadict_bookid['book_ids']=book_ids
            complete_series_list.append(series_datadict_bookid.copy())
        log.info("Database accessed and series data retrieved")
        log.info("Finished getting all books linked to series")
    
        #print(complete_series_list)
        #write to csv
        df=pd.DataFrame(complete_series_list)
        df.to_csv('series_list.csv',sep=',')
        log.info("Finished writing series list to csv")
        #print("series_list.csv written")
    def pagecount(self): # !moved to webscraper, remove from here
        log.info("Getting page count for tag list")
        #get number of pages in the tag list
        url=self.tag['tag_url']
        
        pass
    def db_genrecount(self):  
        log.info("Getting genre count")
        cursor =self.cursor
        genrecount=0
        #print("Database created and Successfully Connected to SQLite")
        log.info('Connected to SQLite Database')
        log.info("Getting genre count")
        cursor.execute("SELECT COUNT(*) FROM tags")
        record = cursor.fetchall()
        for row in record:
            genrecount=row[0]
        self.genrecount=genrecount   #return genrecount


       # print("Current amount of genres in the database: ", genrecount)
        msg="Current amount of genres in the database: "+str(genrecount)
        log.info(msg)
    
        
        print("Database connection is closed")
        log.info("Database connection is closed")
        return genrecount
    def db_write_genre(self):
        log.info("Writing genres to database")
        #msg="Attempting to write " add_genrecount"genres to database"
        #log.info
    def not_done(self):
        genre_url="https://www.novelupdates.com/genre-explanation/"
        genre_location={"class":"w-blog-content"}
        genredict={'id':[],'name':[]}
        genrelist=[]
        genreid=self.genrecount+1
        taglist=[]
        #get all genres to list
        openurl=Request(genre_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage=urlopen(openurl).read()

        soup=BeautifulSoup(webpage, 'lxml')
        #print(soup.prettify())
        genres=soup.find_all("b",{'class':'genreexplain'})

        for genre in genres:
            #print(genre.text)
            genredict['name'].append(genre.text)
            genredict['id'].append(genreid)
            genrelist.append(genredict.copy())
            genreid+=1

class webscraper:
    def __init__(self):
        self.genre={'genre_url':"https://www.novelupdates.com/genre-explanation/",'genre_location':{"class":"w-blog-content"}}
        self.tag={'tag_url':"https://www.novelupdates.com/list-tags/?st=1&pg=",'tag_location':{"class":"g-cols wpb_row offset_default staglistall"}}
        self.tag_page_count=self.pagecount()
        self.genrecount=db.db_genrecount(dbc)
    def pagecount(self):
        log.info2("Getting page count for tag list")
        #as the tags are spread over multiple pages, it is neccessary to search multiple pages to get the total number of tags
        url=self.tag['tag_url']
        count_location={'class':"digg_pagination",'style':""}
        page_count=0
        countlist=[]
        #using the url, search fro count_loation and get the number of pages
        openurl=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage=urlopen(openurl).read()
        soup=BeautifulSoup(webpage, 'lxml')
        #find count_location
        #find all a in count_location
        test=soup.find_all("div",count_location)
        for row in test:
            #find all a in count_location
            a=row.find_all("a")
            for row in a:
                if row.text!=' →':
                    count=row.text
                    countlist.append(count)
        page_count=max(countlist,key=int)
        msg=str("Total number of pages for tag list: "+ page_count)
        log.info2(msg)
        return page_count
    def get_genre_list(self):
        log.info2("Getting genre list")
        url=self.genre['genre_url']
        msg="Getting genres from: "+str(url)
        log.debug2(msg)
        genre_location=self.genre['genre_location']
        
        genrelist=[]
        genreid=self.genrecount+1
        #get all genres to list
        openurl=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage=urlopen(openurl).read()
        soup=BeautifulSoup(webpage, 'lxml')
        genres=soup.find_all("b",{'class':'genreexplain'})
        for genre in genres:
            genredict={'id':[],'name':[]}
            genredict['name'].append(genre.text)
            genredict['id'].append(genreid)
            genrelist.append(genredict.copy())
            genreid+=1
        log.info2("Finished getting genre list")
        #print(genredict)
        #write to csv
        df=pd.DataFrame(genrelist)
        df.to_csv('genre_list.csv',sep=',')
        log.info2("Finished writing genre list to csv")
        
        return genrelist
    def get_tag_list(self):
        #for each page, get the tags and add them to the list
        log.info2("Getting tag list")
        tag_location=self.tag['tag_location']
        taglist=[]
        for i in range(1,int(self.tag_page_count)+1):
            url=self.tag['tag_url']+str(i)
            msg="Getting tag list from page: "+url
            log.info2(msg)
            #url=url+str(i)
            print('Currently searching url:',url, ', iterator i= ',i)
            openurl=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage=urlopen(openurl).read()
            soup=BeautifulSoup(webpage, 'lxml')
            #find tag_location
            test=soup.find_all("div",tag_location)
            for row in test:
                #find all a in tag_location
                a=row.find_all("a")
                for row in a:
                    taglist.append(row.text)
            time.sleep(3)
        log.info2("Finished getting tag list")
        print(taglist)
        #write to csv
        df=pd.DataFrame(taglist)
        df.to_csv('tag_list.csv',sep=',')
        log.info2("Finished writing tag list to csv")
        #print("tag_list.csv written")
    def main(self):
        self.get_tag_list()
        self.get_genre_list()
        

if __name__=="__main__":
    dbc=db()
    #dbc.db_genrecount()

    wbsc=webscraper()
    wbsc.get_genre_list()

        
    
'''    def cursor(input):
        db=self.db
        cursor=db.cursor()
        query=input
        cursor.execute(query)
        result=cursor.fetchall()
        print(result)
'''
