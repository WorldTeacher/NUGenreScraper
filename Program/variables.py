import os
import re
import sys
import glob

'''
Declare variables used in the script
'''

items=glob.glob('/run/media/alexander/Samsung T5/Linux/Full Library/**/*.opf', recursive=True)

test=glob.glob('**/*.opf', recursive=True)
datafield_node_path='{http://www.idpf.org/2007/opf}'
