import variables
import re
from bs4 import BeautifulSoup
import glob

def append_tags():
    add_list=1
    data=glob.glob('/home/alexander/GitHub/NUGenreScraper/Program/test.txt',recursive=True)#variables.test_copy
    orig_file=variables.test
    print(orig_file)
    #print(data)
    '''for i in orig_file:
        print(i)
        with open(i, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
            for tag in soup.find_all('calibre:'):
                if tag.string in variables.list:
                    tag.string=tag.string.replace(tag.string, variables.listrepl[add_list])
                    add_list+=1
                    print(tag.string)
                else:
                    print('not found')
            with open(i, 'w') as file:
                file.write(soup.prettify())'''
    for i in variables.test:
        with open(i,'r') as f:
            tags=['test3','test4']
            #find meta for tags and add content to it
            soup=BeautifulSoup(f, 'lxml')
            #print(soup)
            for meta in soup.find_all('meta'):
                if meta.get('name')=='calibre:user_metadata:#tags':
                    dict={'val':[]}
                    #split meta.get(name) into a list
                    splitter=meta.get('content')[1:-1]
                    #split splitter at the ':'
                    print(splitter)
                    '''splittered=splitter.split(':')
                    #append variables.tags to splittered[1]
                    for tag in tags:
                        splittered[1]=splittered[1]+'"'tag
                    print(splittered)
'''

if __name__=='__main__':
    append_tags()