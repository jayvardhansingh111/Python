# Types of Variables : Three variable

# 1. instance variables - Object level variables
# 2. static variables - Class level
# 3. locals variables - Method level


# --------------------------------------------------------------------------
# # 1. instance variables - Object level variables
# Each object (instance) gets its own copy
# Used to store data specific to an object

# How to declare :-------------------
# Defined - inside constructor using self
#         - inside instance method using self variable

class Employee:
    def __init__(self):
        self.eno=10       # instance variable
        self.ename='jay'   # instance variable
        self.esal=2000    # instance variable

e=Employee()
print(e.__dict__)  # show all instance variable
print(e.eno)



class Test:
    def __init__(self):
        self.a=10  # instance variable

    def m1(self):
        self.b=20   # instance variable

t=Test()
print(t.__dict__)

t=Test()
t.m1()
t.c=30        # instance variable
print(t.__dict__)

t1=Test()
t2=Test()
t1.m1()
t2.x=33
print(t.__dict__)
print(t2.__dict__)


# How to access instance variables :-------------------
class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        print(self.a)
        print(self.b)

t=Test()
t.m1()
print(t.a)
print(t.b)


#  how to delete instance variable ---------
# del self.variable name

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
        self.e=50

    def m1(self):
        del self.b

t=Test()
t.m1()
print(t.__dict__)
del t.a
print(t.__dict__)





class Test:
    def __init__(self):
        self.a=10

    def m1(self):
        self.a=333
        self.b=20

t=Test()
t.m1()
print(t.__dict__)
t.b=999
t.c=888
print(t.__dict__)




class Test:
    def __init__(self):
        self.a=10
        self.b=20
t1=Test()
t1.a=222
t2=Test()
t2.b=555
print(t1.a,t1.b)
print(t2.a,t2.b)




# ------------------------------------------------------------------------------
# # 2. static variables - Class level
#                    only one copy will be created

class Test:
    a=10                # static variable
    def __init__(self):
        self.b=20  # instance variable

print(Test.a) # without creating the object we can access

t1=Test()
t1.b=777
Test.a=888
t2=Test()
print(t2.a,t2.b)
print(t1.a,t1.b)





class Test:
    a=10                # static variable
    def __init__(self):
        self.b=20       # instance variable


t1=Test()
t1.b=777
t1.a=888
t2=Test()
print(t2.a,t2.b)
print(t1.a,t1.b)



# --------------------------------------------------------------------
# Various places to declare static variable

# 1. Inside class directly
# 2. inside constructor by using class name
# 3. inside instance method by using class name
# 4. inside class method by using cls variable or class name
# 5. inside static method by using class name
# 6. outside class by using class name

# class Test:
#     def __init__(self):
#         pass
#     def m1(self):
#         insance method
#
#     @classmethod
#     def m2(cls):
#         class method
#
#     @staticmethod
#     def m3(): pass
#         # static method


class Test:
    a=10             # static variable
    def __init__(self):
        Test.b=20   # static variable
    def m1(self):
        Test.c=30   # static variable

    @classmethod
    def m2(cls):
        Test.d=40  # static variable
        cls.e=50   # static variable

    @staticmethod
    def m3():
        Test.f=60  # static variable

print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
Test.m2()
Test.m3()
Test.g=70       # outside  static variable
print(Test.__dict__)




class Test:
    a=777
    def __init__(self):
        self.a=222
t=Test()
print(t.a)



# -----------------------------------------------
# Accessing static variable :-----
# inside constructor : either by self or class  name
#

class Test:
    a=10

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):         #instance method
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

print(Test.a)
t=Test()
print(t.a)
t.m1()
t.m2()
t.m3()




# ----------------------------------------------
# Modify value of static variable ---

# by using class name
# inside classmethod by using cls variable


class Test:
    a=10      # static variable

    def __init__(self):
        a=888     # local variable

        self.a=40  # instance variable
        Test.a=30  # static variable

        # print(a)
        # print(self.a)
        # print(Test.a)

    def m1(self):
        Test.a=222

    @classmethod
    def m2(cls):
        cls.a=111

    @staticmethod
    def m3():
        Test.a=2222

t=Test()
print(t.a)
t.m1()
print(t.a)

# -----------------------------------

class Test:
    a=10  #Static variable

    def __init__(self):
        a=20           # local variable
        self.a=30      #instance variable
        Test.a=888     # static variable

        print(a)
        print(self.a)
        print(Test.a)

    def m1(self):
        pass

    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass

t=Test()
print(t.a)
print(Test.a)

# ----------------------------------------

class Test:
    a=10  #Static variable

    def __init__(self):
        Test.a=111     # static variable

    def m1(self):
        Test.a=222

    @classmethod
    def m2(cls):
        cls.a=333
    @staticmethod
    def m3():
        Test.a=444

t=Test()
print(t.a)
t.m1()
print(t.a)
t.m2()
print(t.a)
t.m3()
print(t.a)

t.a=999     # declaring instance variable
print(Test.a)
print(t.a)  # it always provide instance variable
Test.a=888 # declare static variable




# ------------------------------------------

class Test:
    a=10
    def m1(self):
        self.a=888

t1=Test()
t1.m1()
print(Test.a)
print(t1.a)


# ------------------------------------------

class Test:
    x=10
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()

print(t1.x,t1.y)
print(t2.x,t2.y)

t1.x=888
t1.y=999
print(t1.x,t1.y)
print(t2.x,t2.y)



# ------------------------------------------

class Test:
    a=10
    def __init__(self):
        self.b=20

t1=Test()
t2=Test()
Test.a=888
t1.b=999
print(t1.a,t1.b)
print(t2.a,t2.b)


 # ------------------------------------------

class Test:
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        self.a=888
        self.b=999

t1=Test()
t2=Test()
t1.m1()

print(t1.a,t1.b)
print(t2.a,t2.b)


 # ------------------------------------------

class Test:
    a=10
    def __init__(self):
        self.b=20

    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999

t1=Test()
t2=Test()
t1.m1()

print(t1.a,t1.b)
print(t2.a,t2.b)
print(Test.a,Test.b)



# -----------------------------------------
# how to delete static variable

# del className.variableName
# del cls.variableName

class Test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a
        cls.b=20
Test.m1()

print(Test.__dict__)
del Test.b
print(Test.__dict__)


# ------------------------------------

class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b

    @classmethod
    def m2(cls):
        cls.d=40
        del Test.c
    @staticmethod
    def m3():
        Test.e=50
        del Test.d

t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
t.m2()
print(Test.__dict__)
t.m3()
print(Test.__dict__)



# -----------------------------
class Test:
    a=20

t=Test()
del t.a  # cant delete through error
del Test.a

print(t.__dict__)







# ---------------------------------------------------------------------------------------------------------------
# # 3. locals variables - Method level
# use for temporary uses / storage within the method


class Test:
    def m1(self):
        a=1000  # local variable
        print(a)

    def m2(self):
        b=2000  # local variable
        print(b)

        # print(a)   # error
t=Test()
t.m1()
t.m2()







