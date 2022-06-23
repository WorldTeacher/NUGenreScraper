import variables
import re
from bs4 import BeautifulSoup
import time
import pandas as pd
data=[]
pathdict={'index':[],'series':[],'id':[]}
opffile=variables.items
x=0 #counter for index
for f in opffile:
    x+=1
    #pathdict['path']=f
    pathdict['index']=x
    foldername=f.split('/')[5]#split the path to the correct folder
    bookidmatch=re.search('\d+(?=\))',foldername)
    bookid=bookidmatch.group(0)
    pathdict['id']=bookid
    with open(f, 'r') as fi:
                soup=BeautifulSoup(fi, 'lxml')
                for meta in soup.find_all('meta'):
                    if meta.get('name')=='calibre:series':
                        name=meta.get('content')
                        if name not in pathdict['series']: #add it
                            pathdict['series']=name
                            data.append(pathdict.copy())
                        else:
                            pathdict['series']=name
                            data.append(pathdict.copy())
#print(data)
datacopy=data
sorted_data=[]
#datacopy.sort(key=lambda z: z['series'])
seriesdict={'index':[],'series':[],'ids':[]}
df=pd.DataFrame(datacopy)
df = df.groupby("series")["id"].apply(", ".join).reset_index()
df_string=df.to_csv("out2.csv",sep=';')
print(df_string)
