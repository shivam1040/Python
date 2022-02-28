func=lambda a:a+5 #pass function as arguement usinfg lambda
print(func(5))

l=["a", "b", "c"]
print(" and ".join(l)) #adds and to end of every element in list l, joins strings only

a="k"
b="j"
c="this {1} and {0}".format(a, b) #old version of f string, 1 0 define the position
print(c)
