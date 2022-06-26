import variables
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from lxml import html
from googlesearch import search
import time
import glob
import pandas as pd
import os

'''
This is an attempt at the scraper for NU.
It should get the tags and genres, add them to a dict with the corresponding bookid and add those to a list which would then be added to the calibre db
'''


class NUScraper:
    def __init__(self):
        #self.path=os.getcwd()
        self.data = []
        self.serieslist = {'series': [], 'path': []}
        self.replacelist=variables.replacelist
        self.taglist=[]
        self.alltaglist=[]
        self.alltags={'tags':[],'bookid':[],'id':[]}
        self.decensor=variables.sorting
        #self.main()
        #print(self.path)
    
    def testing(self):#testing individual functions and merged functions will be done here
        self.make_datalist()
        
                    

    def make_datalist(self):
        '''
        This function does the following:
        1. it takes a look at the Calibre Library folder and for each .opf file (the place where calibre stores metadata as backup)
        2. using the opf file and it's folderpath, it extracts the Series name and database id of the book
        3. using this data, it creates a .csv file for further use 
        '''
        data=[]
        pathdict={'index':[],'series':[],'id':[]}
        opffile=variables.Calibre_opf_files
        x=0 #counter for index
        for f in opffile:
            x+=1
            pathdict['index']=x
            foldername=f.split('/')[5]#split the path to the correct folder
            bookidmatch=re.search('\d+(?=\))',foldername)
            bookid=bookidmatch.group(0)
            pathdict['id']=bookid
            with open(f, 'r') as fi:#extract Series from opf file
                        soup=BeautifulSoup(fi, 'lxml')
                        for meta in soup.find_all('meta'):
                            if meta.get('name')=='calibre:series':
                                name=meta.get('content')
                                if name not in pathdict['series']: #add it
                                    pathdict['series']=name
                                    data.append(pathdict.copy())
                                else:
                                    pathdict['series']=name
                                    data.append(pathdict.copy())
        #make csv with list for further provessing
        df=pd.DataFrame(data)
        df = df.groupby("series")["id"].apply(", ".join).reset_index()
        df.to_csv("sortedlist.csv",sep=';')
    def remove(self):
        files=glob.glob(self.path + '*.csv',recursive=True)
        print('files',files)
        for file in files:
            os.remove(file)
    def main(self):
        '''
        This function does the following:
        1.
        1. it makes a list for the ids of all books associated with the series
        2. for each series, it searches the web and return the first result, which will be used to grab the tags and genres
        3. the grabbed tags and genres will be written to the database
        '''
        file="/home/alexander/GitHub/NUGenreScraper/sortedlist.csv"
        #self.make_datalist()
        csv=pd.read_csv(file,header=1,sep=';')
        for row in csv.iterrows():
            idlist=[]
            idlist.append(row[1][2])
            print(idlist)
            seriesname=row[1][1]
            domain='novelupdates.com'
            lookup='"' + seriesname + '" ' + domain
            print(lookup)

            #time.sleep(3)
            results = search(lookup, tld="com", num=10,stop=1, pause=3) #search for the query, and return the first n results
            time.sleep(3)
            for result in results:
                if 'novelupdates.com/series/' in result:
                    #remove the comment-page-2/ comment-page-3/ comment-page-4 from the link
                    result=result.replace('comment-page-*','')
            print(result)

            




if __name__ == '__main__':
    nuscraper=NUScraper()
    nuscraper.main()