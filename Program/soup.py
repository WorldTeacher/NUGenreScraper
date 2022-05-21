from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re
import time
import glob

'''
Testing only
'''
page=glob.glob('./**/*.html', recursive=True)
paths='/run/media/alexander/Samsung T5/Linux/Full Library'

def Search():
    soup=BeautifulSoup(open(item), 'html.parser')
    genres=soup.find_all('meta')
    for genre in genres:
        value=genre.get('content')
        neededtype=genre.get('property')
        if neededtype=='genre':
            print(value)

def generator(path):
    items=glob.glob(path+'/**/*.epub', recursive=True)
    for i in items:
        print(i)
    
    




if __name__=='__main__':
    generator(paths)
    
