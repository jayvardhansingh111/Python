# OOPs : ----- IN python everything is a object
#
# class -- blueprint of plan / object
# Object -- instance of class
#
#
# class has -- attributes/ properties - Variables , behaviour/actions - methods

# -----------------------------------------
# how to define a python class -----
# class ClassName:
#     ''' documenting string '''
#
#
#     ''' variables - instance variables , static and locals variables
#     methods - instance method , static methods , class methods
#     '''


#class Student:            # not working
#    ''' This is student class '''
#    print(Student.__doc__)
#    print(help(Student))



# 1. instance variables - Object level variables
# 2. static variables - Class level
# 3. locals variables - Method level


#   1. instance method
#   2. static methods
#   3. class methods

class Student:
    ''' hi '''
    def __init__(self):   # constructed
        self.name='jay'
        self.age=20
        self.marks=58

    def talk(self):
        print("hello i am",self.name)
        print("may age",self.age)
        print("my marks",self.marks)

s=Student()  # s is the reference variable for Student() class
# print(s)
s.talk()
print(s.marks)




class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def talk(self):
        print("hello i am", self.name)
        print("may age",self.roll)
        print("my marks",self.marks)
s1=Student('jay',41,7)
s1.talk()

s2=Student('ravi',23,90)
s2.talk()



# ------------------------------------------
# self --  it is a python provided implicit variable
#          always pointing to the current object

# self should be first parameter in constructor

# we can use any name in the place of self but self is recommended

class Student:
    def __init__(sunny,name,roll,marks):
        sunny.name=name
        sunny.roll=roll
        sunny.marks=marks

    def talk(sunny):
        print("hello i am", sunny.name)
        print("may age",sunny.roll)
        print("my marks",sunny.marks)
s1= Student('jay', 41, 7)
s1.talk()

s2= Student('ravi', 23, 90)
s2.talk()




# ==================================================================
#
#  Constructor concept
#
# ===================================================================================================
#
#  Constructor concept --- special method in python
# 1. the name of the constructor should be __init__
# 2. it is called / executed when the object is created
# 3. ment for  initialize the object
# 4. it executed only once


class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def talk(self):
        print("hello i am", self.name)
        print("may age",self.roll)
        print("my marks",self.marks)
s1=Student('jay',41,7)
s1.talk()

s2=Student('ravi',23,90)
s2.talk()





class Test:
    def __init__(self):
        print("constructor execution.")
        print(id(self))

obj=Test()
obj1=Test()
obj2=Test()
obj.__init__()


class Employee:
    def __init__(self,eno, ename, esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd

    def display(self):
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee salary :",self.esal)
        print("Employee address :",self.eadd)


e1=Employee(10,'jay',2000,'gwl')
e2=Employee(20,'singh',2000,'etw')
e3=Employee(30,'bhanu',5000,'DD Nagar')

e1.display()
e2.display()
e3.display()




class Test:
    def __init__(self,x):
        print("constructor execution.")
        print(id(self))

t=Test(100)
t.__init__(20)



# No method overloading or constructor overloading
# class Test:
#     def __init__(self,x):
#         print("No- arg constructor .")
#
#     def __init__(self,x):
#         print("Arg constructor.")
#
# t=Test()
# t.__init__()






class Movie:
    def __init__(self,name,hero,heroine,rating,):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.rating=rating

    def info(self):
        print("Movie name:",self.name)
        print("Hero name:",self.hero)
        print("heroine name:",self.heroine)
        print("rating:",self.rating)

movies=[
    Movie("Bahubali","prabhas","anushaka",99),
    Movie('spider','mahesh','rakul',70),
    Movie('sultan','salman','anushaka',80),
    Movie('rayan','dhanush','rashi',95)
]

# print(movies.info())
for movie in movies:
    movie.info()
    print('--'*20)
    movie.info()




# --------------------------------------------------------
# Diff between method and constructor
#
# 1. method name can be anything
# 1. constructor name should be __init__
#
# 2. method should be called explicitly
# 2. constructor will be executed automatically , not need to call
#
# 3. per object , method can be called any times
# 3. per object , constructor can be called only once




# -------------------------------------------
#  without constructor

class Movie:
     def info(self):
        print("Movie name:",self.name)
        print("Hero name:",self.hero)
        print("heroine name:",self.heroine)
        print("rating:",self.rating)

m=Movie()
m.name='bhahubali'
m.hero='prabhash'
m.heroine='anushaka'
m.rating=98

m.info()






class Movie:
    def info1(self,name,hero,heroine,rating):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.rating=rating

    def info2(self):
        print("Movie name:",self.name)
        print("Hero name:",self.hero)
        print("heroine name:",self.heroine)
        print("rating:",self.rating)

m=Movie()
m.info1('spider','tom','cute',95)
m.info2()



