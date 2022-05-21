from bs4 import BeautifulSoup
from urllib.request import urlopen
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
page=glob.glob('./**/*.html', recursive=True)
paths='/run/media/alexander/Samsung T5/Linux/Full Library'
namespaces='{http://www.idpf.org/2007/opf, http://purl.org/dc/elements/1.1/}'

class NUScraper:
    def __init__(self):
        self.namespaces=namespaces
        #self.localopffile=glob.glob(path+'/*.opf', recursive=True)
        #self.opffile.sort()
        self.opffile=variables.items
        self.data=[]
        self.serieslist={'series':[],'path':[]}
        
        search_term=self.data
    def listgen(self):
        opffile=variables.items
        serieslist={'series':[],'path':[]}
        for f in opffile:
            #append f to the serieslist path
            serieslist['path']=f

            with open(f, 'r') as fi:
                soup=BeautifulSoup(fi, 'lxml')
                for meta in soup.find_all('meta'):
                    if meta.get('name')=='calibre:series':
                        if meta.get('content') =='HumbleBundle Books'or meta.get('content') =='Python':
                            serieslist['series']='No Series'
                            continue
                        serieslist['series']=meta.get('content')
            self.data.append(serieslist)
    def tbd(): #to be done, not yet implemented, will be used to search for genres and tags in webpage
        soup=BeautifulSoup(open(item), 'html.parser')
        genres=soup.find_all('meta')
        for genre in genres:
            value=genre.get('content')
            neededtype=genre.get('property')
            if neededtype=='genre':
                print(value)
    
    

        #print(data)               
            
    def Search(self):#search google for series + novelupdates, to be done
        data=self.data
        print('Data:', data)

if __name__=='__main__':
    NUScraper.listgen(NUScraper)
    NUScraper.Search(NUScraper)
   # NUScraper.Search(search_term=NUScraper.data)
    #print(self.data)
    #NUScraper.Search(NUScraper)
#if __name__=='__main__':
 #   listgen(opffile=variables.items)
    
    
