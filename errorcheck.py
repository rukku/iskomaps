
#build list of files
def listAsc():
    ascList = open('asc.list.txt','wt')
    #ascList = []
    for r,d,f in os.walk("."):
        for files in f:
            if files.endswith(".html"):
                print os.path.join(r,files) 
                out = os.path.join(r,files) + "\n" 
                ascList.write(out)

#check