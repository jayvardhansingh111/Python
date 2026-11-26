# Inheritance --   the properties of parent class can access by child class


# -------------------
# member of one class used inside another class

# 1. By composition ( HAS-A Relationship)
# 2. BY Inheritance ( Is-A Relationship)

# ----------------------------------------------------------------------------------
# 1. By composition ( HAS-A Relationship)

# by using class name or by creating object we can access member of one class inside
# another class .

class Engine:
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        print("Engine specific functionality.")

class Car:
    def __init__(self):
        self.engine=Engine()

    def m2(self):
        print("Class car using class engine functionality.")
        # print(Engine.a)
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c=Car()
c.m2()




class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getInfo(self):
        print("Car name:",self.name)
        print("car model:",self.model)
        print("car color :",self.color)

class Employee:
    def __init__(self,eno,ename,car):
        self.eno=eno
        self.ename=ename
        self.car=car

    def empInfo(self):
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee Car Information .......")
        self.car.getInfo()

c=Car('Innova','2.5v','Gray')
emp=Employee(100,'jay',c)
emp.empInfo()







class X:
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        print("m1 method of x class.")

class Y:
    c=30
    def __init__(self):
        self.d=40

    def m2(self):
        print("m2 method of y class.")

    def m3(self):
        x=X()
        print(x.a)
        print(x.b)
        x.m1()

        print(self.c)
        print(self.d)
        self.m2()
        print("inside m3 method of Y class")

y=Y()
y.m3()









# ---------------------------------------------------------------------------------------------------------
# # 2. BY Inheritance ( Is-A Relationship)
# IS-A Relationship --  parent to child class relationship
# Reusability of code
# ---------------------------------------------------------------------------------------------------------


# class child_class(parent_class)

class Parent:
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        self.c=30
        print("parent class instance method :",self.c)

    @classmethod
    def m2(cls):
        cls.d=40
        print('parent class method :',cls.d)

    @staticmethod
    def m3():
        e=50
        print("Parent class static method.",e)

class Child(Parent):
    pass

c=Child()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()







class P:
    def m1(self):
        print('parent class method')

class C(P):
    def m2(self):
        print('child class method.')

c=C()
c.m1()
c.m2()







class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    c=30
    def __init__(self):
        super().__init__()  # without this line it would not work
        self.d=40

c=C()
print(c.a,c.b,c.c,c.d)






class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat_n_drink(self):
        print("Eat biryani and drink water")

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def work(self):
        print("coding python")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee age:",self.age)
        print("Employee eno:",self.eno)
        print("Employee esal:",self.esal)
        print("Employee Name:",self.name)

e=Employee('jay',32,100,10000)
e.empinfo()

e.eat_n_drink()
e.work()







# -============================================================================================================----
# IS-A vs Has-A  --

# extend existing functionality with some extra functionality --- Is-A
# Dont want to extend just want to use ----     Has-A



class Car:
    def __init__(self,car_name,model,color):
        self.car_name=car_name
        self.model=model
        self.color=color

    def getinfo(self):
        print("Car Information:")
        print("\t Car Name:{}. \n\t Model:{}. \n\t Color:{}.".format(self.car_name,self.model,self.color))

class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat_n_drink(self):
        print("Eat biryani and drink water")

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car

    def work(self):
        print("coding python")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee age:",self.age)
        print("Employee eno:",self.eno)
        print("Employee esal:",self.esal)
        print("Employee Name:",self.name)

        self.car.getinfo()

c=Car("Range Rover","2.5ev","grey")
e=Employee('jay',32,100,10000,c)
e.empinfo()

e.eat_n_drink()
e.work()






# ----------------------------------------------------------------------------
# Composition  vs  Aggregation --  both have Has-A relationship
# Composition -- strong relation
# Aggregation  -- Weak Relaton

class Student:
    college_name='ITMGwalior'
    def __init__(self,name):
        self.name=name

print(Student.college_name)
s=Student("NewITM")
print(s.name)
print(s.college_name)








# ======================================================================================
# Types of Inheritance
#
# 1. Single Inheritance
# 2. Multi Level Inheritance
# 3. Hierarchical Inheritance
# 4. Multiple Inheritance
# 5. Hybrid Inheritance
# 6. Cyclic Inheritance




# --------------------------------------
# 1. Single Inheritance -- (one to one)properties of one class to another class
# Parent-child -- only one

class Parent:
    def m1(self):
        print("parent class method..")

class Child(Parent):
    def m2(self):
        print("child class method")

c=Child()
c.m1()
c.m2()



# ----------------------------------------------
# 2. Multi Level Inheritance -- one parent derived by a child class and that child class derived by another child class

class Parent:
    def m1(self):
        print("parent class method..")

class Child(Parent):
    def m2(self):
        print("child class method")

class SubChild(Child):
    def m3(self):
        print("sub child class method..")

sc=SubChild()
sc.m1()
sc.m2()
sc.m3()





# -----------------------------------------------
# 3. Hierarchical Inheritance -- one parent multiple child

class Parent:
    def m1(self):
        print("parent class method..")

class Child1(Parent):
    def m2(self):
        print("child 1 class method")

class Child2(Parent):
    def m3(self):
        print("child 2 class method")


c1=Child1()
c1.m1()
c1.m2()
# c1.m3()   # cant accessible here

c2=Child2()
c2.m1()
# c2.m2()   # cant accessible here
c2.m3()




# ---------------------------------------------
# 4. Multiple Inheritance  -- (many to one) multiple parent one child


class Parent1:
    def m1(self):
        print("parent 1 class method..")

class Parent2:
    def m2(self):
        print("Parent 2 class method")

class Child(Parent1,Parent2):
    def m3(self):
        print("child class method")
        self.m1()
        self.m2()


c1=Child()
c1.m1()
c1.m2()
c1.m3()






class Parent1:
    def m1(self):
        print("parent 1 class method..")

class Parent2:
    def m1(self):
        print("Parent 2 class method")

class Child(Parent1,Parent2):
    pass

c1=Child()
c1.m1()


class Child(Parent2,Parent1):
    pass

c1=Child()
c1.m1()






# ------------------------------------------------------------
# 5. Hybrib Inheritance -- more than one inheritance using
#  combination of two inheritance


# hybrid inheritance uses MRO algorithm


class Parent1:
    def m1(self):
        print("parent 1 class method")

class Parent2:
    def m2(self):
        print("parent 2 class method")

class Child(Parent1,Parent2):
    def m3(self):
        print("child class method")

class Child1(Child):
    def m4(self):
        print("child 1 class method")

c=Child1()
c.m1()
c.m2()
c.m3()
c.m4()



# --------------------------------------
# 6. Cyclic Inheritance -- no support , not in python
# class c(c):
#   pass



