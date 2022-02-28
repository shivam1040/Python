import import1
while(True):
    print("q to quit")
    a=input("number enter: ")
    if a=="q":
        break

    try:
        a=int(a)
        if a>6:
            print("greater than 6")
    except Exception as e: # at the place of Exception ValueError, ZeroDivisionError etc. keywords can be used to specify typ of errors
        print(e)
    else: #gets printed only when try is succesful
        print("yes") 

print("thanks")

def inc(n):
    try:
        return int(n)+1
    except:
        raise ValueError("bad") #raises an exception with message, self defined exception
        exit()
    finally: #gets executed no matter what
        print("end1")

print(inc(1))
print(import1.num1(2))

a=3

def fu1():
    global a #way to change global variable, even if same variable is initiallized locally, changes are made in global variable 
    print(a)
    a=4
    print(a)

fu1()
print(a)

a=[1,2,3]

for index, item in enumerate(a): #enumerate is used to print to data at once in a list
    print(item, index)

a=[1,2,3,4,5,6]
b=[i for i in a if i%2==0] #shortcut to print store even numbers fromb a, list comprehension
print(b)

s={i for i in a} #set creation shortcut
print(s)
