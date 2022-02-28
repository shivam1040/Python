class Employee:
    company="ABB"
    abx=800

    def details(self):
        self.__class__.company="ABBch" #changes class attribute, ABBch can be replaced with parameter from object
        print("This is ",self.company)
    
    @classmethod
    def changeclassatt(cls):
        cls.company="ABB12" #another way to change class attribute, can take parameter insted of ABB12
    
    @property #getter method, using this decoratorar a function can be used a an attribute, and usecase:to change a class attribute using object attribute
    def det1(self):
        return 700
    
    @det1.setter #setter method decorator
    def det1(self, val):
        self.abx=val
    
    def __init__(self, num):
        self.num=num

    def __add__(self, num1): #overloading to adc two variables, paramet 1 and 2 are passed to construc then add funct to sum
        print("operating") #use mul to multiply, sub fo subtract, truediv for division, floordiv for double slash operation
        return self.num + num1.num
    
    def __str__(self):
        return "ABG"

class Free:
    company="New"

class Programmer(Free, Employee): #inheritance syntax, use comma to inherit multiple classes
    skill="project"
    #company="ABB1"
    
    def __init__(self):
        print("Construc")

    def getskill(self):
        print("Skill is ") #self.skill)

class Retire(Programmer):
    
    skill="retir"
    def getskill(self):
        super().getskill() #call the function of preceeding class, variable check priority is still applicable
        super().__init__()
        print("Skill is ", self.skill)  

a=Employee(1)
d=Employee(2)
a.details()
b=Programmer()
b.getskill() 
b.details() #use of inheritance to call function of base class, CAN BE Overwritten too
print(b.company) #prints the variable company, checks in derived class then base class, priority is alway given to the first class given in parameter while printing variable or functions of of base classes
# multilevel inheritance is inheratnce in chain, and the precceding base class is given priority when data isnt foind in derived class
c=Retire()
c.getskill()
a.det1=900 #sets the value of property/getter method
print(a.abx) #retuns the value of abx after executing setter method
print(a+d) #operator overloading
print(a) #prints str overloading when an object is printed else address is printed

class Compl: #complex number problem
    
    def __init__(self, r, i):
        self.r=r
        self.i=i
    
    def __add__(self, c): #ONE set variable in self and one set in c
        return Compl(self.r+c.r, self.i+c.i) #returning object of th same class
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

e=Compl(1,2)
f=Compl(1,2)
print(e+f)

class Vec:

    def __init__(self, v):
        self.v=v
    
    def __str__(self):
        str1=""
        index=0
        for i in self.v:
            str1+=f"{i}a{index} +"
            index+=1
        return str1[:-1]    
    
    def __add__(self, v2):
        v1=[]
        for i in range(len(self.v)):
            v1.append(self.v[i]+v2.v[i])
        return Vec(v1) #ivokes str func after passing v1 list as object to class vec
    
    def __len__(self):
        return len(self.v)

v3=Vec([1,1])
v4=Vec([1,1])
print(v3+v4)
print(len(v3))