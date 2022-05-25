'''
here are deleted snippets i might reuse in the future
'''

def test(self):
        print(self.link)        


    def print(self, var):
        if var =='result':
            print(self.data)
    def replmap(self, list):
        #cen_list=variables.censors
        #rep_list=variables.listrepl
        #testlist=['S*x S*aves', 'Interc**rse', 'R*pe', 'S*aves', 'F*llatio', 'H*ndjob', 'M*sturbation', 'An*l', 'Prostit**es', 'S*x S*aves', 'Weak to Strong']
        clean_list=[]
        replacelist=variables.replacelist
        cen_list=list
        print('cenlist', cen_list)
        #repl={'old':[],'new':[]}
        #for each entry in censored list, append to old in repl

        #for i in cen_list:
        #    if '*' in i:
        #        repl['old'].append(i)
        #    else:
         #       continue
        #cen_list.append('Consentual S*x')
        #for each entry in replacement list, append to new in repl
        #for i in rep_list:
         #   repl['new'].append(i)
        #print(repl)
        #print(testlist)
        #replace each occurence of repl['old'] with repl['new'] in testlist
        '''for i in testlist:
            for j in repl['old']:
                if j in i:
                    #testlist.remove(i)
                    clean_list.append(i.replace(j,repl['new'][repl['old'].index(j)]))
        #if there is no * in the entry, append to clean_list
        for i in testlist:
            if '*' not in i:
                clean_list.append(i)'''
        for word in cen_list:
            #if word has a * in it, replace it with the corresponding entry in repl['new'], add the words that do not match as well
            # if word has no * in it, add it to clean_list
            if '*' in word:
                if word in replacelist['old']:
                    #replace word with repl['new'][repl['old'].index(word)]
                    newword=word.replace(word, replacelist['new'][replacelist['old'].index(word)])
                    clean_list.append(newword)
            elif '*' not in word:
                newword2=word
                clean_list.append(newword2)
        print(clean_list)
