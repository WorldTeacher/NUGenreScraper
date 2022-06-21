
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import time
import variables
from googlesearch import search
from lxml import html
import variables

'''
Testing only
'''


class NUScraper:
    def __init__(self):
        self.data=[]
        self.serieslist={'series':[],'path':[]}
        self.tags=['manual editing needed']
        self.result=[]
        self.link=[]
        self.censoredlist=variables.list
        self.replacelist=variables.replacelist
        self.sort=variables.sorting
        self.taglist=[]
        self.alltaglist=[]
        self.alltags={'tags':[],'bookid':[],'id':[]}
        #self.sorting=input('sort? (y/n) '  )
        
    def etacalc(self):
        #this is a rough estimate on how long it will take to complete the process
        #it is based on the number of opf files in the specified Calibre Library Folder, and the current delays
        #it is not accurate
        opffile=variables.items
        
        opfcount=len(opffile)
        eta=opfcount*4 #this is the pure delay of the search, processing not included
        eta_h=eta/3600
        print('The script will now search metadata for '+str(opfcount)+' novels.')
        print('This will take at least '+str(round(eta_h))+' hours.') 

        #print('opf count: '+str(opfcount))

    def get_opf_path(self):#this function gets the path to all opf files in the specified Calibre Library Folder
        #get_opf_count()
        opffile=variables.items
        pathdict={'index':[],'path':[],'series':[],'id':[]}
       
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
                        pathdict['series']=meta.get('content')
                        self.data.append(pathdict.copy()) 
   
    def Search_links(self): #this function searches for the link to the novels based on the result of get_opf_path()
        #search_term=self.data
        
        for name in self.data:
            #query=name['series']
            
            query='overgeared' #example for testing
            domain='novelupdates.com' #what page to search, only novelupdates.com is supported, but other sites could be added (PR welcome)
            '''if query=='Python' or query =='HumbleBundle' or query=='Japanese':
                tags=['manual editing needed']
                self.add_tags(tags)'''
            lookup=query + " " + domain
            #print('looking for: ',query)
            results = search(lookup, tld="com", num=10,stop=10, pause=2) #search for the query, and return the first 10 results
            time.sleep(2)
            # displaying the searched result links
            '''for result in results:
                print(result)'''
            self.result=results
            #return self.result

    def Search_linkstest(self): #this function searches for the link to the novels based on the result of get_opf_path()
        search_term=self.data
        
        for name in search_term:
            #query=name['series']
            print(name['series'])

        query='overgeared' #example for testing
        domain='novelupdates.com' #what page to search, only novelupdates.com is supported, but other sites could be added (PR welcome)
        '''if query=='Python' or query =='HumbleBundle' or query=='Japanese':
            tags=['manual editing needed']
            self.add_tags(tags)'''
        lookup=query + " " + domain
        #print('looking for: ',query)
        results = search(lookup, tld="com", num=10,stop=10, pause=2) #search for the query, and return the first 10 results
        time.sleep(2)
        # displaying the searched result links
        '''for result in results:
            print(result)'''
        self.result=results
        #return self.result
    def find_link(self): #this function finds the link to the novel based on the result of Search_links(); basic cleanup is done
        for result in self.result:
            if 'novelupdates.com/series/' in result:
                link=result
                self.link=link
                #print('link: '+self.link)
                return self.link

    def get_tags(self):
        remove=['/comment-page-2/','comment-page-3/', 'comment-page-4']
        query=self.link
        for entry in remove:
            if entry in query:
                query=query.replace(entry,'')
        print(query)
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
        
        tags=soup.find("div", {"id": 'showtags'})
        for tag in tags:
        #remove everything in <>
            tag=re.sub('<[^>]*>', '', str(tag))
            #print(tag)
            if tag== ' ':
                continue
            elif tag=='\n':
                continue
            else:
                if '*' in tag:
                    tag=tag.replace(tag,self.replacelist['new'][self.replacelist['old'].index(tag)])
                    self.taglist.append(tag)
                else:
                    self.taglist.append(tag)
    

    def get_tagstest(self):
        remove=['/comment-page-2/','comment-page-3/', 'comment-page-4']
        

        query=self.link
        for entry in remove:
            if entry in query:
                query=query.replace(entry,'')
        print(query)
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
        
        tags=soup.find("div", {"id": 'showtags'})
        for tag in tags:
        #remove everything in <>
            tag=re.sub('<[^>]*>', '', str(tag))
            #print(tag)
            if tag== ' ':
                continue
            elif tag=='\n':
                continue
            else:
                if '*' in tag:
                    tag=tag.replace(tag,self.replacelist['new'][self.replacelist['old'].index(tag)])
                    self.taglist.append(tag)
                    #add to alltags
                    self.alltags['tags'].append(tag)
                else:
                    self.taglist.append(tag)
                    self.alltags['tags'].append(tag)
        print(self.alltags)
        #if self.sorting =='y':
        #    self.sort_tags()
            
        #self.replmap(list=taglist)
        print('genres: '+str(genrelist))
        print('tags: '+str(self.taglist))
    def sort_tags(self):
        #this function ,if enabled, sorts the tags into multiple lists to make the calibre tags sorted
        sortedlist=[]
        sortlist=['Protagonist','Magic','Adapted','Game-like Elements']
        for sorter in sortlist:
            for tag in self.taglist:
                if sorter in tag:
                    if 'Adapted' in tag:
                        self.taglist.remove(tag)
                        addtag='Adaptation'+'.'+tag
                        sortedlist.append(addtag)
                    elif sorter =='Game-like Elements':
                        tags=['MMORPG','Level','Game Ranking System']
                        self.taglist.remove(tag)
                        addtag='Game-like Elements'+'.'+tag
                        sortedlist.append(addtag)
                    else:
                        self.taglist.remove(tag)
                        addtag=sorter+'.'+tag
                        sortedlist.append(addtag)

                else:
                    self.taglist.remove(tag)
                    addtag=tag
                    sortedlist.append(addtag)
        
        print('sortedlist: '+str(sortedlist))
    def main(self):
        #scraper=NUScraper()
        self.get_opf_path()
        #for i in range(0,len(self.data)):
        #    self.Search_links()
        #    self.find_link()
        #    self.get_tags()
            #self.data[i]['tags']=self.taglist
            #self.taglist=[]
        self.Search_linkstest()
        self.find_link()
        self.get_tagstest()
        
if __name__=='__main__':
    
    #print('calculating ETA...')
    scraper=NUScraper()
    #scraper.etacalc()
    #time.sleep(0.5)
    #cont=input('Do you want to continue? (y/n): ')
    #if cont=='y':
    #    scraper.main()
    #else:
    #    print('exiting')
    #    exit()
    scraper.Search_linkstest()
    scraper.find_link()
    scraper.get_tagstest()
    #dec=True
    #dec=input('Should I censor the tags? (True or False):')
    #scraper.main(dec=input('Should I censor the tags? (True or False):'))
    #scraper.replmap()