from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import time

link='https://www.novelupdates.com/list-tags/?st=1&pg='
page=1
taglist=[]
while page <=16:
    request=Request(link+str(page), headers={'User-Agent': 'Mozilla/5.0'})
    webpage=urlopen(request).read()
    soup=BeautifulSoup(webpage, 'html.parser')
    
    #print(soup.prettify())
    tag=soup.find('div', {'class': 'wpb_wrapper'})
    for entry in tag:
        
        print(entry)
    page+=1
    time.sleep(5)
print(taglist)
