from googlesearch import search

query='magi craft meister'
domain='novelupdates.com'
lookup=query + " " + domain

result=search(lookup, tld='com',lang='en' ,num=1, start=1)

print(result)