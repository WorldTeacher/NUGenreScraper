from bs4 import BeautifulSoup
import re

html='/home/alexander/GitHub/NUGenreScraper/Program/Shuumatsu Nani Shitemasu ka? Isogashii desu ka? Sukutte Moratte Ii desu ka? - Novel Updates.html'

soup=BeautifulSoup(open(html), 'lxml')
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
    else:
        taglist.append(x)
    
print('genres: '+str(genrelist))
print('tags: '+str(taglist))