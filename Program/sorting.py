from calendar import c
from operator import contains
import variables
from bs4 import BeautifulSoup

'''
This part will be included in the main program to make the tags and genres sorted

#worldbuilding
genre=11
worldbuildlist=[1,2,3,4,5,6,7,8,9,10]
if genre == worldbuildlist:
    gen='holo'
    world=gen+ genre
    print('Worldbuilding added: '+ str(genre) + ' to the list \n')
    print(str(world))
else:
    print('Worldbuilding not added: '+ str(genre) + 'to the list \n')
    '''

'''
how it should work:
1. get count of opf files in the directory
2. for each opf file:
    2.1 get the series name
    2.2 get the path
    2.3 append the series name and path to the data list
3. return the data list
'''   

def get_opf_count():
    opffile=variables.items
    count=0
    for f in opffile:
        count+=1
    #return count
    print(count)

def get_opf_path():
    #get_opf_count()
    opffile=variables.items
    pathdict={'index':[],'path':[],'series':[]}
    safe=[]
    safe1=[]

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
                    safe1.append(pathdict.copy()) 
                    #print(safe1)       
        #print(pathdict)
        
    print(safe1)


def listgen():
        opffile=variables.items
        series=[]
        path=[]
        serieslist={'series':[],'path':[]}
        series={'series':[],'path':[]}
        data=[]
        for f in opffile:
            #append f to the serieslist path
            series['path']=f
            #serieslist['path'].append(f)

            with open(f, 'r') as fi:
                soup=BeautifulSoup(fi, 'lxml')
                for meta in soup.find_all('meta'):
                    if meta.get('name')=='calibre:series':
                        series['series'].append(meta.get('content'))
                        data.append(series)
                        #serieslist['series'].append(meta.get('content'))
                        #series.append(meta.get('content'))
                        #data.append(serieslist)
                        #print(path)
                        #time.sleep(0.3)
                        #print(data)
                        #data.append(serieslist)  
        #data.append({'series':series,'path':path})
                                      
        #return self.data
        print(data)

def testing():
    count=1
    name='Magi Craft Meister'
    loc='/run/'
    test=[]
    series={'index':[],'series':[],'path':[]}
    series['index'].append(count)
    series['series'].append(name)
    series['path'].append(loc)
    test.append(series)
    #print(test)
    for name in test:
        for serie in name['series']:
            print(serie)

if __name__=='__main__':
    testing()