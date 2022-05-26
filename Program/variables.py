import os
import re
import sys
import glob

'''
Declare variables used in the script
'''

items=glob.glob('/mnt/sd/Full Library/**/*.opf', recursive=True)
test_copy=glob.glob('/home/alexander/GitHub/NUGenreScraper/Program/* copy.opf', recursive=True)
test=glob.glob('/home/alexander/GitHub/NUGenreScraper/Program/metadata.opf', recursive=True)

datafield_node_path='{http://www.idpf.org/2007/opf}'
page=glob.glob('./**/*.html', recursive=True)
paths='/run/media/alexander/Samsung T5/Linux/new Full Library'
namespaces='{http://www.idpf.org/2007/opf, http://purl.org/dc/elements/1.1/}'
list=['Interc**rse','S*x', 'Weak to Strong','Petty Protagonist']
listrepl=['First Time Intercourse','Intercourse','Sex', 'Rape','Slaves','Fellatio','Handjob','Masturbation','Anal','Prostitutes','Sex Slaves']
censors=['First Time Interc**rse','Interc**rse','S*x','R*pe','S*aves','F*llatio','H*ndjob','M*sturbation','An*l','Prostit**es','S*x S*aves']
replacelist={'old': ['First-time Interc**rse', 'Interc**rse', 'S*x', 'R*pe', 'S*aves', 'F*llatio', 'H*ndjob', 'M*sturbation', 'An*l', 'Prostit**es', 'S*x S*aves'], 'new': ['First-time Intercourse', 'Intercourse', 'Sex', 'Rape', 'Slaves', 'Fellatio', 'Handjob', 'Masturbation', 'Anal', 'Prostitutes', 'Sex Slaves']}

'''
Real Variables below this, to be implemented later on
'''

Calibre_Library_Path='/mnt/sd/Full Library/'
#in Calibre_Library_Path, find all opf files

Calibre_opf_files=glob.glob(Calibre_Library_Path+'**/metadata.opf', recursive=True)
replacelist={'old': ['First-time Interc**rse', 'Interc**rse', 'S*x', 'R*pe', 'S*aves', 'F*llatio', 'H*ndjob', 'M*sturbation', 'An*l', 'Prostit**es', 'S*x S*aves'], 'new': ['First-time Intercourse', 'Intercourse', 'Sex', 'Rape', 'Slaves', 'Fellatio', 'Handjob', 'Masturbation', 'Anal', 'Prostitutes', 'Sex Slaves']}
#If a new replacelist is needed, or if tags need to be added, run the replacechange.py script
sorting=True