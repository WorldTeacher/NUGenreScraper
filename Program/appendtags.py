import variables
import re
from bs4 import BeautifulSoup
import glob
import json

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
        f=open(i,'r')
        data=f.read()
        f.close()
        
        tags=['test3','test4']
        #find meta for tags and add content to it
        soup=BeautifulSoup(data, 'lxml')

        for meta in soup.find_all('meta'):
            if meta.get('name')=='calibre:user_metadata:#tags':
                metastr=str(meta)
                
                #dict={'val':[]}
                #split meta.get(name) into a list
                splitter=meta.get('content')
                #print(meta.find('content'))
                splitterjson=json.loads(splitter)
                splitterjson['#value#']=tags
                splitterstr=str(splitterjson)
                #print(splitterstr)
                splitterstr=splitterstr.replace("\'","\"")

                #print(meta)
        
        #print(data.replace(metastr,splitterstr))
        print(data.find(metastr))
        #f=open(i,'w')
       # f.write(data.replace(,splitterstr))
        #f.close()

        #f=open(i,'w')
        #f.write()
if __name__=='__main__':
    append_tags()