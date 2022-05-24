from mailbox import NoSuchMailboxError
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re
import time
import glob
import xml.etree.ElementTree as ET
import variables
from googlesearch import search
import requests
from lxml import html

'''
Testing only
'''
page=glob.glob('./**/*.html', recursive=True)
paths='/run/media/alexander/Samsung T5/Linux/new Full Library'
namespaces='{http://www.idpf.org/2007/opf, http://purl.org/dc/elements/1.1/}'

class NUScraper:
    def __init__(self):
        self.namespaces=namespaces
        #self.localopffile=glob.glob(path+'/*.opf', recursive=True)
        #self.opffile.sort()
        self.opffile=variables.items
        self.data=[]
        self.serieslist={'series':[],'path':[]}
        self.tags=['manual editing needed']

    def add_tags(self):
        pass

    def get_opf_path(self):
        #get_opf_count()
        opffile=variables.items
        pathdict={'index':[],'path':[],'series':[]}
       
        x=0
        for f in opffile:
            x+=1
            pathdict['path']=f
            pathdict['index']=x
            with open(f, 'r') as fi:
                soup=BeautifulSoup(fi, 'lxml')
                for meta in soup.find_all('meta'):
                    if meta.get('name')=='calibre:series':
                        pathdict['series']=meta.get('content')
                        self.data.append(pathdict.copy()) 
                        #print(safe1)       
            #print(pathdict)
            
        


   
    def Search(self):
        search_term=self.data
        for name in self.data:
            query=name['series']
            domain='novelupdates.com'
            if query=='Python' or query =='HumbleBundle' or query=='Japanese'
                tags=['manual editing needed']
                self.add_tags(tags)
            lookup=query + " " + domain
            print('looking for: ',query)
            results = search(lookup, tld="com", num=10,stop=10, pause=2)
            time.sleep(2)
            # displaying the searched result links
            for result in results:
                print(result)
            
if __name__=='__main__':
    scraper=NUScraper()
    scraper.get_opf_path()
    scraper.Search()
    #scraper.Search()
    #NUScraper().Search()
    
    
