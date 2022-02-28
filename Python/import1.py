def num1(num):
    return num+1
if __name__=="__main__": #if the file is imported to other then everything is run no matter one func call or many, to avoid that this can be used. makes sure code is run only when executed from this file not in the ones exported to
    num=input("enter number1: ")