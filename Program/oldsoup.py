# importing the search function from
# the googlesearch library
from googlesearch import search
# The text that we want to query
p1='sword art online'
p2='novelupdates.com/series'
p3=p1 + " " + p2
query = "magi craft meister novelupdates"
# using the search() function to search for the text in google
results = search(p3, tld="co.in", num=10,stop=1, pause=2)
# displaying the searched result links
for result in results:
    print(result)