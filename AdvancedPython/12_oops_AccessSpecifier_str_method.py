# public , private , protected variables


# ---------------------------------------------------------------------------------
# public ------  by default every member is public in python

class Test:
    a=10 # public variable
    def m1(self):
        self.b=20

print(Test().a)
t=Test()
# print(t.b)



# ---------------------------------------------------------------------------------
# protected --- it is available within the call or its child class

class Test:
    _x=10             # protected variable
    def __init__(self):
        self._y=20

t=Test()
print(t._x)
print(t._y)



#  ---------------------------------------------------------------------------------
# private) -- its available within the class

# spacial way --  object._className__variable

class Test:
    __x=10             # private variable
    def __init__(self):
        self.__y=20
        print(self.__x)
        print(self.__y)

t=Test()
# print(t.__x)  # error , cant access
# print(t.__y)  # cant access

print(t._Test__x)   # valid , can access

print(Test.__dict__)





# ===========================================================================================================

#  __str__()  -- to return meaning full string object we have to override __str__() method


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student('jay', 10)
s2 = Student('ravi', 20)
print(s1) # <__main__.Student object at 0x000002CBFECC7CB0>
print(s2) # <__main__.Student object at 0x000002CBFEF67110>


# -------------------------

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def __str__(self):
        return 'This the student name is :{}, and roll number :{}'.format(self.name,self.roll)

s1=Student('jay',10)
s2=Student('ravi',20)

print(s1)  #This the student name is :jay, and roll number :10
print(s2)  #This the student name is :ravi, and roll number :20





#---------------------------------------------------------------------------------------------

# repr()  -- repr() return a string containing a printable representation od object


#  in string - string to object is possible but object to string is not possible

import datetime
today=datetime.datetime.now()
s=str(today)  # obj to str
print(s)
# d=eval(s)  # string to obj , not possible
# print(d)




#  in string - string to object is possible but object to string is not possible

import datetime
today=datetime.datetime.now()
s=repr(today)  # obj to str
print(s)
d=eval(s)  # string to obj
print(d)
print(type(d))






# ===========================================================================================================
# Bank application

class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance=self.balance-amount
        else:
            print("Insufficient balance.")

    def print_statement(self):
        print("Account Balance:",self.balance)

class CurrentAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=2000)

    def __str__(self):
        return "{} 's current account balance is : {}.".format(self.name,self.balance)

class SavingsAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{} 's current account balance is : {}.".format(self.name, self.balance)


c=CurrentAccount('jay',10000)
print(c)
c.deposit(20000)
print(c)
c.withdraw(20000)
print(c)

print()
s=SavingsAccount('jay',10000)
print(s)
s.deposit(5000)
print(s)
s.withdraw(10000)
print(s)


