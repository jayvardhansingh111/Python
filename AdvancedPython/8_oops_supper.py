# super()  -- supper is an in build function ,
#            which can be used to call parent class
#         constructors methods and variables from child class

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Student name:", self.name)
        print("student age:", self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):

        super().__init__(name, age)

        self.rollno=rollno
        self.marks=marks

    def display(self):
        super().display()
        print("student roll number:",self.rollno)
        print("student marks:",self.marks)


s=Student('jay',20,41,60)
s.display()






# ---------------------------
class P:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Parent Instance method")

    @classmethod
    def m2(cls):
        print("parent class method")

    @staticmethod
    def m3():
        print("parent static method")

class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c=C()






# -------------------------------------
# how to call method of a particular super class


class A:
    def m1(self):
        print("A class m1 method")

class B(A):
    def m1(self):
        print("B class m1 method")

class C(B):
    def m1(self):
        print("C class m1 method")

class D(C):
    def m1(self):
        print("D class m1 method")

class E(D):
    def m1(self):
        print("E class m1 method")
        super().m1()
        super(C,self).m1()   # particular B class method call
        super(B,self).m1()   # call A


e=E()
e.m1()







# ------------------------------------

class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    a=777
    def m1(self):
        print(super().a)
        # print(super().b)     # error
        print(self.b)  # 20   valid

        self.b=888
        print(self.b)     # 888
        super().__init__()
        print(self.b)   # 20



c=C()
c.m1()







#  From class method of child class, how to call parent class instance methods and constructor

class A:
    def __init__(self):
        print("parent class constructor")

    def m1(self):
        print("parent class instance method")

class B(A):
    @classmethod
    def m2(cls):
        print("child class ,class method")

        super(B,cls).__init__(cls)
        super(B,cls).m1(cls)

B.m2()







# How to call parent class static method from child class static method

class A:

    @staticmethod
    def m1():
        print("parent class static method")

class B(A):

    @staticmethod
    def m2():
        print("child class static method")
        super(B,B).m1()

B.m2()



