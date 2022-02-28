def per(x=2): #syntax for a func in python taking and returning x, if user provides no value then default value 2 wiil be returned
    return x

print(per("c")) #calling a function, return wont print a value

def fac(n):
    if n==1 or n==0:
        return 1
    else:    
        return n*fac(n-1) #he return value is stored and then itera begin again with n-1 until if condition is met, so that the final multiplication with 1 gets done
print(fac(5))