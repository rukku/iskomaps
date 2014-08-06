
ascFile = open('placelist.txt')
placelist = []

#for shed
#t1 = ".spot-%s { background-position:-130px 0px; }" 
#t2 = ".spot-%s.active { background-position:-130px -120px; }"


#for normal
t1 = ".spot-%s { background-position:-780px 0px; }" 
t2 = ".spot-%s.active { background-position:-780px -120px; }"


for line in ascFile.readlines():
	if ("shed" in line):
		continue
	else:
		id = line[:-1]
		print t1 % (id) 
		print t2 % (id)
		
