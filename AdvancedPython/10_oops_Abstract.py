# # Abstract method -- don`t know the about the implementation, still we can declare a method
# # the method which has only declaration not implementation
# # implemented in child class method
#
#
# from abc import *
# class Vehicle:
#     @abstractmethod
#     def get_no_of_wheels(self):
#         pass
#
# class Fruit:
#     @abstractmethod
#     def get_taste(self):pass



# # -------------------------------------------------------------------------------------------
# # Abstract class -- partially implemented class called abstract class
#
# how to declare abstract class explicitly -- we have to extend ABC (Abstract Base Class) class


# from abc import  *
# class Vehicle(ABC):
#     pass
# v=Vehicle()




# from abc import  *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):pass
#
# t=Test()
# t.m1()
#
#
#
# from abc import  *
# class Test:
#     @abstractmethod
#     def m1(self):pass
#
# t=Test()
# t.m1()





# ------------------------------------------------------------

# abstract class with 0 abstract method
from abc import  *
class Test(ABC):
    def m1(self):
        print('m1 , no abstract method')

t=Test()
t.m1()






# ------------------------------------------------------------
# cant create obj for the child class if the parent class abstract method not define in child class

from  abc import *
class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass

class Bus(Vehicle):
    pass

b=Bus()  #TypeError: Can't instantiate abstract class Bus without an implementation for abstract method 'no_of_wheels'






# -----------------------------------------------
# define in child class

from  abc import *
class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass

class Bus(Vehicle):
    def no_of_wheels(self):
        return 6
class Car(Vehicle):
    def no_of_wheels(self):
        return 4
class Auto(Vehicle):
    def no_of_wheels(self):
        return 3

b=Bus()
print(b.no_of_wheels())

a=Auto()
print(a.no_of_wheels())

c=Car()
print(c.no_of_wheels())

b=Bus()







from abc import *
class P(ABC):
    @abstractmethod
    def m1(self):pass

    @abstractmethod
    def m2(self):pass

class C(P):
    def m1(self):
        print('m1 implementation')
class CC(C):
    def m2(self):
        print('m2 implementation')

c=CC()
c.m1()
c.m2()






