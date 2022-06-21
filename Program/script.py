import variables
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from lxml import html
from googlesearch import search
import time
import pandas as pd

'''
This is an attempt at the scraper for NU.
It should get the tags and genres, add them to a dict with the corresponding bookid and add those to a list which would then be added to the calibre db
'''


class NUScraper:
    def __init__(self):
        self.data = []
        self.serieslist = {'series': [], 'path': []}
        self.censoredlist=variables.list
        self.replacelist=variables.replacelist
        self.taglist=[]
        self.alltaglist=[]
        self.alltags={'tags':[],'bookid':[],'id':[]}
        self.make_datalist()
    
    def testing(self):#testing individual functions and merged functions will be done here
        self.make_datalist()
        for entry in self.data:
            query=entry['series']
            domain='novelupdates.com' #what page to look for
            lookup=query + ' ' + domain
            results = search(lookup, tld="com", num=10,stop=10, pause=2) #search for the query, and return the first 10 results
            time.sleep(2)
            for result in results:
                if 'novelupdates.com/series/' in result:
                    #remove the comment-page-2/ comment-page-3/ comment-page-4 from the link
                    result=result.replace('comment-page-2/','')
                    

    def make_datalist(self):
        pathdict={'index':[],'path':[],'series':[],'id':[]}
        opffile=variables.items
        x=0 #counter for index
        for f in opffile:
            x+=1
            pathdict['path']=f
            pathdict['index']=x
            foldername=f.split('/')[5]#split the path to the correct folder
            foldername=re.sub('[a-zA-Z]','',foldername)   #remove all letters from the folder name
            foldername=foldername.replace(' ','')#remove whitespaces
            foldername=re.sub('[^\(0-9)]','',foldername)#remove all non-numbers from the folder name
            foldername=foldername.split('(')[1]
            foldername=foldername.split(')')[0] 
            pathdict['id']=foldername
            with open(f, 'r') as fi:
                soup=BeautifulSoup(fi, 'lxml')
                for meta in soup.find_all('meta'):
                    if meta.get('name')=='calibre:series':
                        name=meta.get('content')
                        if name not in pathdict['series']: #add it
                            pathdict['series']=name
                            self.data.append(pathdict.copy())
                        else:
                            pathdict['series']=name
                            self.data.append(pathdict.copy()) 
        print(self.data)  
    def main(self):
        self.make_datalist()


if __name__ == '__main__':
    nuscraper=NUScraper()