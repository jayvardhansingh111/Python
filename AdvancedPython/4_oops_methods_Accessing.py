# Methods -> those function which are defined inside the class

# Types of methods :-----
# -------------------------------------------
# 1.instance method
# 2.class methods
# 3. static methods

# -------------------------------
# 1.instance method  -- object related method
#  using  instance variable  inside a method is called instance method

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("hi",self.name)
        print("your marks are:",self.marks)

        s.grade() # call the method

    def grade(self):
        if self.marks>=60:
            print("you got first grade.")
        elif self.marks>=50:
            print("you got second grade.")
        elif self.marks>=35:
            print("you got third grade.")
        else:
            print("you are failed.")


s=Student('jay',70)
s.display()
# s.grade()

s=Student('jay',40)
s.display()


#  ---------------------------
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.display()
    def display(self):
        print("hi",self.name)
        print("your marks are:",self.marks)

        self.grade() # call the method

    def grade(self):
        if self.marks>=60:
            print("you got first grade.")
        elif self.marks>=50:
            print("you got second grade.")
        elif self.marks>=35:
            print("you got third grade.")
        else:
            print("you are failed.")


s=Student('jay',70)
s1=Student('jay',40)


# ---------------------------------------
#  Setter and Getter method

# setter/ mutator methods to set the value of instance variables
# Getter / Accessor methods to get the value of instance variables

class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return  self.name

    def set_marks(self,marks):
        self.set_marks=marks

    def get_marks(self):
        return self.set_marks

# s=Student()
l=[]
n=int(input("Enter number of student:"))
for i in range(n):
    s=Student()
    name=input("Enter name of student:")
    marks=int(input("Enter the marks of student:"))
    s.setName(name)
    s.set_marks(marks)
    l.append(s)

# print(l) # provide the student l object

for i in l:
    print("\nstudent name:",s.getName())
    print("student marks:",s.get_marks())
    print()






# --------------------------------------------------------
# 2.class methods -- inside method we are using static variable or class level variable
# not using instance variable

# @classmethod  -- decorator used to declare class method
# m1(cls) -- method should take cls variable

class Animal:
    legs=4

    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
        print(name,"walks with",Animal.legs,"legs")

Animal.walk('dog')


# ------------------------------------
# want to count number of object created for a class

class Test:
    count=0 # static variable
    def __init__(self):
        Test.count += 1

    @classmethod
    def no_obj_created(cls):
        print("number of object created:",Test.count)

t1=Test()
t2=Test()
Test.no_obj_created()
t3=Test()
t4=Test()
Test.no_obj_created()







# ------------------------------------------------------------
# 3. static methods -- inside method we are not using instance and static variable
# it is general utility method

# @staticmethod -- decorator used to declare


class DurgaSirMaths:

    @staticmethod
    def add(x,y):
        print("the sum is:",x+y)

    @staticmethod
    def product(x,y):
        print('the product is:',x*y)

    @staticmethod
    def average(x,y):
        print('the average is:',(x+y)/2)

DurgaSirMaths.add(10,20)
DurgaSirMaths.product(10,20)
DurgaSirMaths.average(10,20)




# -------------------------------------
# no decorator in the method then what happened

# instance method : no decorator
# class method : @classmethod
# static method: @staticmethod


# Test.m1() -- static method
# t.m1() -- instance method


class Test:
    def m1(cls):
        print("some method.")
        print(id(cls))

Test.m1('jk')  # static method  -- calling by class name
t=Test()
t.m1()      # instance method  -- calling by class object
print(id(t))









# ==================================================================================================
# Accessing ----  member of one class inside another class

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print('Employee number:',self.eno)
        print('Employee name:',self.ename)
        print('Employee salary:',self.esal)

class Test:
    def modify(emp):
        emp.esal=emp.esal + 1000
        emp.display()


e=Employee(100,'jay',10000)
Test.modify(e)
Test.modify(Employee(200,'jk',400))







# ==================================================================================================
# Inner class -- class inside another class

class University:
    class Department:
        pass

class Car:
    class Engine:
        pass



class Outer:
    def __init__(self):
        print('outer class creation')

    class Inner:
        def __init__(self):
            print('inner class creation')

        def m1(self):
            print('inner class method')

        class InnerInner:
            def __init__(self):
                print('inner inner method creation')

            def m2(self):
                print('inner inner class method')



o=Outer()
i=o.Inner()
i.m1()

o=Outer().Inner()
o.m1()

o=Outer.Inner().m1()

o=Outer.Inner().InnerInner().m2()




# ------------------------------------------------

class Human:
    def __init__(self):
        self.name='jay'
        self.head=self.Head()
        self.brain=self.head.Brain()

    def display(self):
        print('hello',self.name)
        self.head.takl()
        self.brain.think()

    class Head:

        def takl(self):
            print('talking....')

        class Brain:
            def think(self):
                print('thinking..')

h=Human()
h.display()



# -------------------------------------------

class Person:
    def __init__(self,name,dd,mm,yyy):
        self.name=name
        self.dob=self.Dob(dd,mm,yyy)

    def display(self):
        print('Name:',self.name)
        self.dob.display()      # calling another method of other class

    class Dob:
        def __init__(self,dd,mm,yyy):
            self.dd=dd
            self.mm=mm
            self.yyy=yyy

        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyy))

p=Person('jay',6,7,2008)
p.display()

p.Dob(2,3,2009).display()




# ---------------------------------------------------------------------
# Nested method --- method inside method
# purpose : to define method specific repeatedly required functionality


class Test:

    def m1(self):

        def calc(a,b):
            print('The sum :',a+b)
            print('The sub :',a-b)
            print('The product is:',a*b)
            print('The division:',a/b)
            print()

        calc(10,20)
        calc(100,200)
        calc(1000,2000)

t=Test()
t.m1()






