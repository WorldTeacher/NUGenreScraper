# **NovelUpdates Scraper**

## What is this?

all of this started as a sideproject in order to strengthen my coding expertise and to enrich the metadata of my Light Novel eBook Collection.
The goal is to be able to start the script, let it do it's thing and once it's done have all the tags and genres added to the Light Novels.

### Background information

It started off fairly naively, me not really bothering to check how & where Calibre stores relevant metadata was a large part of it.
This script will take a look at an existing calibre instance / folder and check Novelupdates.com for tags and genres.
At first, I thought I could just store everything in the .opf file and Calibre would just check those and *bam* have the changed metadata in the GUI. But I have now realized that the .opf file is only a backup in case the database breaks (so much for 2 weeks of testing...)

I have now moved on to directly writing to the database (testing only atm) and rewriting the code by splitting it up in smaller functions that do one thing only, so that troubleshooting is easier.

Since this project is open source, anyone should be able to use it, and so, I decided to learn about configuration files and how to use them

**De-censoring** 
I don't really like censored tags, so I decided to go ahead and created a list in the config file with all censored tags. I added a toggle in the config file to change wether or not the program should decensor or not

### *Current Status*

As of right now, the program is only for testing.

It is able to search the web for the title and get the link.

In a testfile, I'm able to access the database and write data to it,  but I have not yet tested it for multiple series and for multiple tags at once.

For the Database write, I'm debating wether or not to store all tags and ids in a dict to make a mass write at the end 
(something like this:
tagwrite=[tag1,tag2,tag3,tagn] (will all be written to tags table)
masswrite=[{tags:[tag1,tag2,tag3,tagn],ids:[id1,id2,id3]},{tags:[tag1,tag3,tag4],ids:[id4,id5,id6]},…]
(for each id, every tag will be linked in the books_tag_link table))

I do not know which method I'll use, but I can imagine the mass write being more performant, since it is one single write operation for all tags and multiple for the ids, but I'll figure that out when it's time for that…