# Function Decorators --
# input function ==> 18_Decorator function ==> output function with extended functionality
# to make our code shorter ,

def decorator(func):
    def inner(name):
        if name=='sunny':
            print("hello sunny bad morning...")
        else:
            func(name)
    return inner

# @decorator  #first method
def wish(name):
    print("hello",name,"good morning")

decor_function=decorator(wish) # second function

wish("jay")
wish("ravi")
wish('sunny')
decor_function("jay")
decor_function("sunny")


#  ---------------------------------------------------------------
def smart_division(func):
    def inner(a,b):
        if b==0:
            print("hello ... how can you divide by zero.......")
        else:
            return func(a,b)
    return inner

@smart_division
def division(a,b):
    return a/b
print(division(10,2))
print(division(10,5))
print(division(10,0))




# --------------------------------------------------------------------------
# 18_Decorator chaining ------------------------

def decorator(func):
    def inner(name):
         print("First decorator function...")
         func(name)
    return inner

def decorator1(func):
    def inner(name):
        print("Second decorator function (decorator1)..")
        func(name)
    return inner

@decorator1  # second decorator calling
@decorator  # first decorator calling
def wish(name):
    print("hello",name,"good morning")

wish("jay")
wish("ravi")
wish('sunny')




# ----------------------

def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor2(func):
    def inner():
        x=func()
        return 2*x
    return inner


@decor2
@decor1
def num():
    return 10
print(num())









# -------------------------------------------------------------------------------------------

l=[x*x for x in range(10)]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l)


# ==================================================================================================================
# -------------------------------------
# generator function -- generates a sequence of values
# generate the value at run time and not storing it in to the memory
# it uses yield keyword
# memory utilization improved, performance will be improved

l=(x*x for x in range(10000))
print(next(l))
print(next(l))
print(next(l))
# for i in l:
#     print(i)
print(type(l))

def mygen():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'

g=mygen()
mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
for i in g:
    print(i)


def countdown(num):
    print("start countdown")
    while num>0:
        yield num
        num=num-1
values=countdown(5)
print(type(values))
for i in values:
    print(i)


#----------------------------------------------------------
import random
import time

name=['sunny','bunny','vinny','jay']
subjects=['python','java','c++']

def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
            'id':i,
            'name': random.choice(name),
            'major': random.choice(subjects)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(name),
            'major': random.choice(subjects)
        }
        yield person



t1=time.time()
people=people_list(10000000)
t2=time.time()

print("list took time",(t2-t1))


t1=time.time()
peoples=people_generator(10000000)
t2=time.time()

print("generator took time",(t2-t1))



# --------------------------------------
# wa generator function to generate first n numbers

def first_number(num):
    n=1
    while n<= num:
        yield n
        n=n+1
values=first_number(7)
# print(values)
for i in values:
    print(i)


# ------------------------------------
# to generate fibonacci numbers

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fibonacci()
for i in f:
    if i>100:
        break
    print(i)


