from functools import reduce #to use reduce function
def sq(n):
    return n*n

l=[1,2,3]

print(list(map(sq, l))) #using map one can use a function on different datatypes, sq is function and l is parameter of it, list is used to convert map object to list

#filter(funct, parameter/list) returns items/param for which returns true in a funct

def check(num):
    if num>3:
        return True
    else:
        return False

l=[1,2,3,4,5,6]
print(list(filter(check, l)))

l=[5,6,25,30,31]
print(list(filter(lambda a:a%5==0, l))) #filters and print numbers in list l divisible by 5

sum=lambda a, b:a+b
print(reduce(sum, l)) #reduce applies rolling computation on a sequential list

print(reduce(max, l)) #prints max in list l by sequentially reducing until last iteration