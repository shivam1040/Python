i=0
while(i<10):
    print(str(i))
    i=i+1

a=[1,2,3]    
for item in a:
    print(item)

for c in range(0,2): #print from 0 to 1
    print(c)
    if(c==5):
        break

for c in range(0,3,2): #print from 0 to 2 and skip every second charac
    print(c)
else: #for can have optional else, can be executed after loop exhausts and wont execute after loop terminates because of break
    print("n")

for c in range(0,7): #print from 0 to 6    
    if(c==5):
        continue # if c==5 then print(c) is skipped and iterations begin again from next value
    print(c)

if (i>0):
    pass #pass is used to execute those statements which need a supporting statement (if, for, while), usecase: comeback later and add statememnts later
while (i>99):
    pass
print("a")

print(f"{i}X{i}={i*i}") # This will print numbers inside braces and perform calculation too, just string formatting and replacement of str)

for d in a:
    if (d==1): #checks element 1 of a if equals to 1
        print("a")

print("g"*(4)) #prints g for 4 times

j=3
for h in range(3):
    print(" "*(j-h-1), end="") #does not print new line and ends with specified charact
    print("*"*(2*h+1), end="")
    print(" "*(j-h-1))
