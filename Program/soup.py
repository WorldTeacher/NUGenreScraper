
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

import re
import time
import glob
import xml.etree.ElementTree as ET
import variables
from googlesearch import search
import requests
from lxml import html
import variables

'''
Testing only
'''


class NUScraper:
    def __init__(self):
        self.namespaces=variables.namespaces
        #self.localopffile=glob.glob(path+'/*.opf', recursive=True)
        #self.opffile.sort()
        self.opffile=variables.items
        self.data=[]
        self.serieslist={'series':[],'path':[]}
        self.tags=['manual editing needed']
        self.result=[]
        self.link=[]
        self.censoredlist=variables.list
        self.replacelist=[]
    

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
            
        


   
    def Search_links(self):
        search_term=self.data
        for name in self.data:
            #query=name['series']
            query='overgeared'
            domain='novelupdates.com'
            '''if query=='Python' or query =='HumbleBundle' or query=='Japanese':
                tags=['manual editing needed']
                self.add_tags(tags)'''
            lookup=query + " " + domain
            print('looking for: ',query)
            results = search(lookup, tld="com", num=10,stop=10, pause=2)
            time.sleep(2)
            # displaying the searched result links
            '''for result in results:
                print(result)'''
            self.result=results
            return self.result

    def find_link(self):
        for result in self.result:
            if 'novelupdates.com/series/' in result:
                link=result
                self.link=link
                print('link: '+self.link)
                return self.link
    def get_tags(self):
        remove=['/comment-page-2/','comment-page-3/', 'comment-page-4']
        query='https://www.novelupdates.com/series/overgeared/comment-page-3/'#
        #if /comment-page-* in query: remove it
        for entry in remove:
            if entry in query:
                query=query.replace(entry,'')
        
        openurl=Request(query, headers={'User-Agent': 'Mozilla/5.0'})
        webpage=urlopen(openurl).read()
        
        soup=BeautifulSoup(webpage, 'lxml')
        #soup=BeautifulSoup(open(html), 'lxml')
        #get meta for genres
        genrelist=[]
        genres=soup.find_all('meta')
        for genre in genres:
            value=genre.get('content')
            neededtype=genre.get('property')
            if neededtype=='genre':
                genrelist.append(value)
        #get meta for tags
        taglist=[]
        tags=soup.find("div", {"id": 'showtags'})
        for tag in tags:
            #remove everythin in <>
            x = re.sub('<[^>]*>', '', str(tag))
            if x == ' ' or x=='\n':
                continue
            if x in self.censoredlist:
                
                taglist.append(x)
            
        print('genres: '+str(genrelist))
        print('tags: '+str(taglist))
    def test(self):
        print(self.link)        


    def print(self, var):
        if var =='result':
            print(self.data)

    def main(self):
        #scraper=NUScraper()
        self.get_opf_path()
        self.Search_links()
        self.find_link()
        self.get_tags()
        
if __name__=='__main__':
    scraper=NUScraper()
    #scraper.main()
    scraper.replmap()