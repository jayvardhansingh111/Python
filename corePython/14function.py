# function -- a group of lines  , most code reusable concept
# there are two types of functions in python
# 1. predefined functions / in built functions
# 2. user defined functions


# # --------------------------------------------------------------------------------------------------------------------------
# # 1. predefined functions / in built functions-------------------------------
# # there are 71 predefined built in functions
# abs()               delattr()           hash()               memoryview()    set()
# all()               dict()              help()               min()           setattr()
# any()               dir()               hex()                next()          slice()
# ascii()             divmod()            id()                 object()        sorted()
# bin()               enumerate()         input()              oct()           staticmethod()
# bool()              eval()              int()                open()          str()
# breakpoint()        exec()              isinstance()         ord()           sum()
# bytearray()         filter()            issubclass()         pow()           super()
# bytes()             float()             iter()               print()         tuple()
# callable()          format()            len()                property()      type()
# chr()               frozenset()         list()               range()         vars()
# classmethod()       getattr()           locals()             repr()          zip()
# compile()           globals()           map()                reversed()      __import__()
# complex()           hasattr()           max()                round()
#
#
# print()
# len()
# eval()
# input()
# id()
# sorted()

#---------------------------------------------------------------------------------------------------------------
# 2. user defined functions
def wish():
    """# body of the function"""
    print("good morning")

wish()
wish()
wish()
# ----------------------------------------------
# arguments in function
def wish(name):
    print("hello",name,"good evening")
wish('jay')
wish('vardhan')



def square(n):
    print("the square of {} is {}".format(n,n*n))
square(10)
square(20)


def add(n,m):
       return n+m
result=add(10,30)
print("the result is",result)
print("the sum is ",add(10,20))



def f1():
       print("hello")
f1()
print(f1)


# --------------------------------------------------------------------------------
# WAP to check weather the number is even or odd
def evenodd(n):
       if n%2==0:
              print("{} number is even".format(n))
       else:
              print("{} number is odd".format(n))
evenodd(10)
evenodd(23)
evenodd(78)


# --------------------------------------------------------------------------------------
# WAP to find factorial of given number
def factorial(n):
       r=1
       while n>=1:
              r= r * n
              n=n-1
       # print(result)
       return r
print(factorial(4))
factorial(5)

for i in range(1,6):
       print("The factorial of {} is {}".format(i,factorial(i)))

# -----------------------------------------------------------------------------------------------
def sum_sub(d, b):
       sum= d + b
       sub= d - b
       return sum , sub
x,y=sum_sub(100,50)
print("the sum:",x)
print("the sub:",y)


def calc(a,b):
       sum = a + b
       sub=a-b
       multi=a*b
       division=a/b
       return sum,sub,multi,division
x,y,p,q=calc(100,30)  # first method
print("the sum is:",x)
print("the sub is:",y)
print("the multiply is:",p)
print("the division is:",q)

t=calc(100,50)    # second method
for i in t:
       print(i)


# --------------------------------------------------------------------------------------------------------
# types of arguments / parameter-----------------
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable length Arguments

# --------------------------------------
# 1. Positional Arguments - change the order result might be changed
def sub(a,b):
       print(a-b)
sub(10,30)
sub(100,20)

# --------------------------------------
# 2. Keyword Arguments -- passes arguments by parameter name ,no order,
def wish(name,msg):
       print("hello",name,msg)
wish(name='jay',msg='good morning')
wish(msg='good evening',name='jay')
wish('jay','good morning.')
wish('jay',msg='good morning')
# wish(msg='good evening','jay')  # error


# --------------------------------------
# 3. Default Arguments
def f1(name="guest"):
       print("hello",name, "good morning.")
f1()
f1('jay')

def f1(msg,name="guest"): # default arguments must be last
       print("hello",name,msg, "good morning.")
f1('jay')



def wish(marks,age,name="guest",msg="good morning"):
       print("student name:",name)
       print("student age:",age)
       print("students marks:",marks)
       print("student msg:",msg)
wish(100,40,'jay')
wish(marks=20,age=23)
wish(100,age=18,msg='good night')




# --------------------------------------
# 4. Variable length Arguments

# wap to print sum of given number
def sum(*a): # by passing any number of arguments
    # print("variable length arguments ")
    result=0
    for i in a:
        result=result+i
    print("the sum is:",result)
sum()
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)



def sum(*a,name): # by passing any number of arguments
    # print("variable length arguments ")
    result=0
    for i in a:
        result=result+i
    print("the sum by:",name,':',result)

sum(name='jay')
sum(10,name='jay')
sum(10,20,name='var')
sum(10,20,30,40,name='singh')


# ------------------------------------------
#  ** for pass multiple arguments
def display(**kwargs):
    print(type(kwargs))
    print("Record information:")
    for k,v in kwargs.items():
        print(k,".....",v)

display(name='jay',marks=100,gf='anju')
display(name='jay',wife1='himanshi',wife2='mushkan')
display(name='jay',brand1='jk',brand2='kj')



def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(2,3,arg3=4,arg4=7)
f(arg1=10,arg2=20)
f(4,5,arg3=5)



#-------------------------------------------------------------------------------------
# types of variable--------
# 1. global variable -- declare outside the function , available for all the functions in that module
# 2. Local variable -- declare inside the function , uses only that lacal function


a=10           # global variable
def f1():
    print("f1 :",a)

def f2():
    b=20        #   local variable
    print("f2 global variable :", a)
    print('local variable:',b)
f1()
f2()

# to declare global variable inside the function we need to global keyword

a=10           # global variable
def f1():
    global a
    a=23
    print("f1 :",a)

def f2():
    b=20        #   local variable
    print("f2 global variable :", a)
    print('local variable:',b)
f1()
f2()



def f1():
    global a
    a=23
    print("f1 :",a)

def f2():
    global a
    a=20        #   local variable
    print("f2 :", a)
def f3():
    print('f3:',a)
f1()
f2()
f3()


# ----------------------------
a=10
def f1():
    a=20
    print(a)
    # print(globals())
    print(globals()['a'])
f1()



# ------------------------------------------------------------------------------------------
# Recursive function -- a function calls the same itself called recursive function
# reduce the length of code, improve readability

print(factorial(3))
# Wap to find factorial by using recursion
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(0))
print(factorial(5))
print(factorial(7))
print(factorial(3))


# ---------------------------------------------------------------------
# Anonymous function --- No name, hidden, name less function
# instant use( only one time use)


# -----------------------------------
# lambda function --------
# lambda input :expression

# wap of lambda function to find square
s=lambda x:x*x
print(s(3))
print(s(5))
print(s(4))


# ---------------------------------------
# wap of lambda to find sum of two number
s=lambda a,b:a+b
print("the sum of {} and {} is: {}".format(10,20, s(10,20)))
print("the sum of {} and {} is: {}".format(100,200, s(100,200)))


# ---------------------------------------
# wap to find which is bigger
s=lambda a,b:a if a>b else b
print("the biggest of {} and {} is: {}".format(10,30,s(10,30)))
print("the biggest of {} and {} is: {}".format(40,30,s(40,30)))
print("the biggest of {} and {} is: {}".format(400,300,s(400,300)))



# ------------------------------------------------
# pass function as a argument to a another function
# ----------------------------------
# 1. filter() -- filtering the required thing from a group
# filter(function,sequence)

def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,2,7,30,35,45,50,60]
print(type(filter(iseven,l)))
list1=list(filter(iseven,l))
print(list1)


l=[0,2,7,30,35,45,50,60]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)


# ------------------------------------------------------------
# 2. map() --
# map(function,sequence)

def double(x):
    return 2*x

l=[0,5,10,15,20,25,30,35,40]
l1=list(map(double,l))
print(l1)

l1=list(map(lambda x:2*x,l))
print(l1)

l1=[1,2,3,4]
l2=[10,20,30,40]
l=list(map(lambda x,y:x*y,l1,l2))
print(l)


# ----------------------------------
# 3. reduce() -- used to reduce sequence of elements in a single element
# reduce(function,sequence)

from functools import reduce

l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)



# --------------------------------------
def f1():
    print("hello")
print(id(f1()))
print(type(f1()))


# -----------------------------------------
# function aliasing
def wish(name):
    print("good morning",name)
wish('jay')

greeting=wish        # function aliasing
greeting('singh')
print(id(wish))
print(id(greeting))

del wish
# wish('jay') # error because it is deleted
greeting('jay')



# ----------------------------------------------------
# Nested function -- function inside another function
def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()



def f1():
    def inner(a,b):
        print("the sum :",a+b)
        print("the average:",(a+b)/2)
    inner(10,20)
    inner(30,40)
    inner(50,20)
    inner(100,200)
f1()



def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function returning inner function")
    return inner
f1=outer() # function call / return value to be assigned
f2=outer # aliasing
f1()


