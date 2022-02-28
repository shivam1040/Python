import os
f=open("s.txt", 'r') # r is switch to read, by default it's r if not specified, use rb to read binary file
data=f.read(2) #prints only two charac, data is read in string form
#data=f.readline() #reads first line, if iterated then consecutive lines too
print(data)
#f.close()
f=open("s.txt", 'w') #use a switch for appending
f.write("Please2") #make sure data written is in str format
f=open("s.txt", 'r') #to perform diff operations make sure opening closing is done
data=f.read()
print(data)
f.close()

with open("s.txt", 'w') as f: #automatically open close file
    a="a"
    print(a)
    i="s"
    f.write(f"{i}") #string formatting can be used here too
    d=["1","2","3"]
    for f in d:
        c=f.replace(f,"1") #replaces ouccurene of  d list in f with "aa"
    while a: #will read line by line until eof of content and can be used to find line  number
        e=f.readline()

os.remove("s,txt") #removes file






