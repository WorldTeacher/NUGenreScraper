import os
import re
import sys
import glob

'''
Declare variables used in the script
'''

items=glob.glob('/mnt/sd/Full Library/**/*.opf', recursive=True)

test=glob.glob('/home/alexander/GitHub/NUGenreScraper/Program/metadata.opf', recursive=True)
datafield_node_path='{http://www.idpf.org/2007/opf}'
