import os

import json

#build list of files




def readPlaces():
    ascFile = open('placelist.txt')
    ascList = []
    for line in ascFile.readlines():
        ascList.append(line)
        print line
	return ascList
	

def listAsc():
    ascList = open('asc.list.txt','wt')
    #ascList = []
    for r,d,f in os.walk("."):
        for files in f:
            if files.endswith(".md"):
                #print os.path.join(r,files) 
                out = os.path.join(r,files) + "\n" 
                ascList.write(out)

def readList():
    ascFile = open('asc.list.txt')
    ascList = []
    for line in ascFile.readlines():
        ascList.append(line)
        print line
        
    return ascList

def	placeCheck(place, placelist):
		if place in placelist:
			return True
		else: 
			return False
	
def process(item, placelist):
	item = item[:-1]
	f = open(item)
	
	errorlist= []
	#print "Processing" + item
	for line in f.readlines():
		if line.find("section id")==1:
			#print line[13:-3]
			id = line[13:-3]
			status = placeCheck(id, placelist)
			if status == False:
				errorlist.append(id)
		else: continue
	return errorlist
		

listAsc()
htmlist = readList()
#placelist =readPlaces()
'''
for item in htmlist:
	#print item
	process(item, placelist)
#check

print len(placelist)


for place in placelist:
	print place
'''
ascFile = open('placelist.txt')
placelist = []
for line in ascFile.readlines():
	placelist.append(line[:-1])

errorcount= 0	
for item in htmlist:
	#print item
	id = process(item, placelist)
	
	if len(id)> 1:
		errorcount = errorcount + 1
		print item, id
print errorcount