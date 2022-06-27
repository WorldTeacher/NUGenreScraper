
import glob
import json


'''
Declare variables used in the script
'''
with open('config.json') as config_file:
    data=json.load(config_file)

#items=glob.glob(path +'/**/*.opf', recursive=True)
db_path=data['calibre']['database_path']
test_copy=glob.glob('/home/alexander/GitHub/NUGenreScraper/Program/* copy.opf', recursive=True)
test=glob.glob('/home/alexander/GitHub/NUGenreScraper/Program/metadata.opf', recursive=True)

datafield_node_path='{http://www.idpf.org/2007/opf}'
page=glob.glob('./**/*.html', recursive=True)
paths='/run/media/alexander/Samsung T5/Linux/new Full Library'
namespaces='{http://www.idpf.org/2007/opf, http://purl.org/dc/elements/1.1/}'
list=['Interc**rse','S*x', 'Weak to Strong','Petty Protagonist']

tags=['test1','test2']
'''
Real Variables below this, to be implemented later on
'''

#Calibre-specific Variables below this line
Calibre_Library_Path=data['calibre']['library_path']
#in Calibre_Library_Path, find all opf files
Calibre_opf_files=glob.glob(Calibre_Library_Path+'**/metadata.opf', recursive=True)


#Tags below this line
#If a new replacelist is needed, or if tags need to be added, add them to the config.json
#censored=data['taglist']['censored']
#uncensored=data['taglist']['uncensored']
#replacelist={'old': censored, 'new': uncensored}
replacelist={'old': ['First-time Interc**rse', 'Interc**rse', 'S*x', 'R*pe', 'S*aves', 'F*llatio', 'H*ndjob', 'M*sturbation', 'An*l', 'Prostit**es', 'S*x S*aves'], 
             'new': ['First-time Intercourse', 'Intercourse', 'Sex', 'Rape', 'Slaves', 'Fellatio', 'Handjob', 'Masturbation', 'Anal', 'Prostitutes', 'Sex Slaves']}
censoring=data['decensor']


