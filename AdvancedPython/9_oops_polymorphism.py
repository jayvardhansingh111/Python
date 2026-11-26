# PolyMorphism -- one name but multiple form

# Poly --- many
# morph --- form

# ------------------------------------------------------------------------
# 1. Duck Typing philosophy of python -- run time polymorphism

# 2. Overloading -- same method name with diff arguments
#           operator overloading
#           method overloading
#           constructor overloading

# 3. Overriding -- same method with same arguments
#           method overriding
#           constructor overriding

# ------------------------------------------------------------------------



# =======================================================================================================================================================
# 1. Duck Typing philosophy of python -- run time polymorphism, it decide the type of boj
#    there is no way to define the type explicitly



class Duck:
    def talk(self):
        print("Quack quack...")
class Dog:
    def talk(self):
        print("Bow bow....")
class Cat:
    def talk(self):
        print("meow meow...")
class Goat:
    def talk(self):
        print("myaah myaah ...")

def f1(obj):
    obj.talk()
l=[Duck(),Dog(),Cat(),Goat()]
for obj in l:
    f1(obj)



# ---------------------------------------------------------
# hasattr() ---- has not attribute to the method then we use

class Duck:
    def talk(self):
        print("Quack quack...")
class Dog:
    def bark(self):
        print("Bow bow....")

def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()

d=Duck()
f1(d)
d1=Dog()
f1(d1)




# =======================================================================================================================================================

# -----------------------------------------------------------------------------

# 1. Overloading -- same method name with diff arguments
#         1.  operator overloading
#         2.  method overloading
#         3.  constructor overloading




# --------------------------------------------------------------------------------------------------------------
# 1. operator overloading --  we can use same operator for multiple purposes

#  +   -- obj.__add__(self,other)
#  -   -- obj.__sub__(self,other)
#  *   -- obj.__mul__(self,other)
#  /   -- obj.__div__(self,other)
#  //  -- obj.__floordiv__(self,other)
#  %   -- obj.__mod__(self,other)
#  **   -- obj.__pow__(self,other)
#  +=  -- obj.__iadd__(self,other)




# class Book:
#     def __init__(self,pages):
#         self.pages=pages
# b1=Book(100)
# b2=Book(200)
#
# print(b1 + b2)  # invalid




class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages + other.pages

    def __mul__(self,other):
        return self.pages * other.pages

b1=Book(100)
b2=Book(200)
print("Total number of pages:",b1 + b2)  # invalid

print(b1*b2)






class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self, other):
        return self.marks>other.marks
    def __ge__(self, other):
        return self.marks>=other.marks
    def __lt__(self, other):
        return self.marks<other.marks
    def __le__(self, other):
        return self.marks<=other.marks


# print('10>20',10>10)   # error

s1=Student('jay',200)
s2=Student('ravi',100)

print('s1>s2 : ',s1>s2)
print('s1>=s2 : ',s1>=s2)
print('s1<s2 : ',s1<s2)
print('s1<=s2 : ',s1<=s2)







class Book :
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
       print("add method calling")
       total= self.pages+other.pages
       return Book(total)
    def __str__(self):
        print("str method calling")
        return str(self.pages)

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(50)

bx=b1+b2+b3
print(bx)
print(b1)
print(b1+b2)
print(b1+b2+b3+b4)








class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return 'this is student with name: {} , marks: {}'.format(self.name,self.marks)

s1=Student('jay',90)
s2=Student('ravi',80)

print(s1)
print(s2)





class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self, other):
        return self.salary * other.days

class TimeSheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

    def __mul__(self, other):
        return self.days * other.salary

e=Employee('jay',500)
t=TimeSheet('jay',25)

print("This is month salary:",e*t)

print("This is month salary:",t*e)






# --------------------------------------------------------------------------------------------------------------

# 2. method overloading -- two method having same name but diff argument

#  in python method overloading is not possible

# if we are trying to declare multiple method with the same name and diff number of
# arguments then python only consider last method previous one deleted internally

class Test:
    def m1(self):
        print("No arguments method")
    def m1(self,a):
        print("One arguments method")
    def m1(self,a,b):
        print("two arguments method")

t=Test()
# t.m1()
# t.m1(10)
t.m1(10,20)





# ----------------------------------------------------

#1. variable length arguments and default arguments
# m1(obj)

# 2. default way arguments




# 2. default way arguments

class Test:
    def sum(self,a=None,b=None,c=None):
        print("one arg method")
        if a != None and b!=None and c!=None:
            print("The sum of 3 number:",a+b+c)
        elif a!=None and b!=None:
            print("The sum of 2 number:",a+b)
        elif a!= None:
            print("the sum of 1 number:",a)
        else:
            print("please provide at least one number ")


t=Test()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,0,30)





# ----------------------------------------------
# 1. variable length arguments and default arguments

class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The sum:',total)

t=Test()
t.sum()
t.sum(10)
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,0,30)
t.sum(10,20,30,40,50)






# --------------------------------------------------------------------------------------------------------------
# 3. constructor overloading -- two constructor in a class with same name


# this code having error
class Test:
    def __init__(self):
        print("no arg constructor")
    def __init__(self,a):
        print("one arg constructor")
    def __init__(self,a,b):
        print("two arg constructor")

# t=Test()  # error
# t=Test(10)  # error
t=Test(10,20)





class Test:
    def __init__(self,a=None,b=None):
        print("constructor with 0|1|2 arguments")


t=Test()
t=Test(10)
t=Test(10,20)



# constructor with any number with arguments
class Test:
    def __init__(self,*a):
        print("constructor with 0|1|2 arguments")


t=Test()
t=Test(10)
t=Test(10,20)
t=Test(10,20,30,40)








# ========================================================================================================================


# 2. Overriding -- if parent and child class have the same name and redefine in child claass
#         1.  method overriding
#         2.   constructor overriding


# --------------------------------------------------------------------------------------------------------------

# 1. Method Overriding --

class P:
    def property(self):
        print('Land+cash+gold+power')
    def marraige(self):
        print('Anju|shivani')

class C(P):
    def marraige(self):
        print('Anju|himanshi')

c=C()
c.property()
c.marraige()





class P:
    def property(self):
        print('Land+cash+gold+power')
    def marraige(self):
        print('Anju|shivani')

class C(P):
    def marraige(self):
        super().marraige()
        print('Anju|himanshi')

c=C()
c.property()
c.marraige()




# --------------------------------------------------------------------------------------------------------------
# 2. constructor overriding

class P:
    def __init__(self):
        print('parent class constructor')

class C(P):
    def __init__(self):
        print('child class constructor')

c=C()






class P:
    def __init__(self):
        print('parent class constructor')

class C(P):
    def __init__(self):
        super().__init__()
        print('child class constructor')
c=C()




class P:pass
class C(P): pass
c=C()

