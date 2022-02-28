class Number:
    
     def sum():
        pass

num=Number() #object of class Number

class Railway:
    Tier="2A" #class attribute
    meal="N"
    
    def __init__(self, X, Y): #constructor, gets executed without function call if no parameter is required
        print("Created")
        self.x=X
        self.y=Y
        print(Y)

    def data(self): #self is same as this in java and relates to current instance of objects
        print(self.name) #self makes sure that name attribute of the calling object gets printed
        print(self.train)
    
    def sal(self, sig): #can take several arguements
        print("100k"+self.meal+sig) #an object gives acces to both class attribut/instance attribute

    @staticmethod #executes below function without passing object/using self
    def hello():
        print("hey")

shiv=Railway(5,6) #giving values for constructor parameter
shiv.name="S"
shiv.train="R"
shiv.meal="Y" #way to initialize attribute of object/instance
shiv.data()
shiv.sal("SIG")
Railway.sal(shiv,"SIG") #same as above line
Railway.Tier="3A" #way to change class attribute
print(shiv.Tier)
print(shiv.meal) #if attribute is present in obj then print else checks in class attribute for result
shiv.hello()
print(Railway.Tier) #way to print a class attribute