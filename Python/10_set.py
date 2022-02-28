a=set() #empty set, a={} creates empty dic
a={1,2,2,3} # non repititive element is set
a.add(1) # add 1 at end of a set
a.add((4,5,6)) # only tuple can be added to set not list or dict, immutable, unindexed
print(len(a)) #print len of set a
a.remove(3) #removes 3 from set
print(a)
a.pop() #removes random element from set
a.clear() #clears set
a.union ({8,11}) #union of s with 8, 11
a.intersection({8,11}) #intersection of s with 8,11
a={20, 20.0, 20.1} # len of set a is 2 since 20=20.0 in python



