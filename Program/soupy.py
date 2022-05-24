from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os
import re
import time
import glob
import xml.etree.ElementTree as ET
import variables
from googlesearch import search

'''
Testing only
'''
def listgen(query):
        
        serieslist={'series':[],'path':[]}
        data=[]
        for f in query:
            #append f to the serieslist path
            serieslist['path']=f

            with open(f, 'r') as fi:
                soup=BeautifulSoup(fi, 'lxml')
                for meta in soup.find_all('meta'):
                    if meta.get('name')=='calibre:series':
                        if meta.get('content') =='HumbleBundle Books'or meta.get('content') =='Python':
                            serieslist['series']='No Series'
                        else:
                            serieslist['series']=meta.get('content')
            data.append(serieslist)
        #return data
        print(data)
                        

def Search():
    remove=['/comment-page-2/','comment-page-3/', 'comment-page-4']
    query='https://www.novelupdates.com/series/overgeared/comment-page-3/'#
    #if /comment-page-* in query: remove it
    for entry in remove:
        if entry in query:
            query=query.replace(entry,'')
        
    openurl=Request(query, headers={'User-Agent': 'Mozilla/5.0'})
    webpage=urlopen(openurl).read()
    soup=BeautifulSoup(webpage, 'html.parser')
    
    #in soup find all genres
    soup.find_all()

if __name__ == '__main__':
    Search()
    