import settings
import time
import os
import glob
def main():
    settingspath=os.path.join(os.path.dirname(__file__), 'settings.py')
    with open(settingspath, 'w') as file:
        
        q1=input('Do any tags need to be added to the replacelist? (y/n): ')
        if q1=='y':
            print("Please enter the old tag in it's censored form (e.g. 'S*x S*aves'), followed by the new tag in it's uncensored form (e.g. 'Sex Slaves)")
            print('only one tag can be added at once')
            q3=input('What is the name of the tag? ')
            #split q3 at ,

            q4=q3.split(sep=',')
            #print(q4[1])
            settings.censors.append(q4[0])
            settings.listrepl.append(q4[1])
            #update settings.py

            print('replacelist: '+str(settings.replacelist))

        if q1=='n':
            print('No tags to add')
            print('exiting')
            time.sleep(0.5)
            exit()

if __name__ == '__main__':
    main()