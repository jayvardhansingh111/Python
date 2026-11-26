# Decorator  --
            #  decorator is a function which can take a function as an argument and
            # extend its functionality and returns modified function with extended functionality





# -----------------------------------------------------------

def f1():
    print("hii")
print(f1())
print(id(f1()))



#  function aliasing
def wish(name):
    print("Good evening:",name)

greeting=wish   # aliasing

wish('jay')
greeting('ravi')

del wish

# wish('jay')   # this one is deleted
greeting('ravi')




def outer():
    print("outer function started")

    def inner():
        print('inner function execution')
    print('outer function calling inner function')
    inner()

outer()
# inner() --> invalid directly calling --> outside  of function






def outer():
    print("outer function started")

    def inner():
        print('inner function execution')
    print('outer function calling inner function')
    return inner

i=outer()
i()


# f1=outer  # --> aliasing
# f1=outer()  #--> calling





#  -----------------------------------------
#  we can pass function as an argument

# filter(function,sequence)
# map(function,sequence)
# reduce()




def is_even(x):
    if x%2==0:
        return True
    else:
        return False

l=[1,2,3,4,5,6,7,8,9]

f=list(filter(is_even,l))
print(f)




def squareit(n):
    return n*n

l=[1,2,3,4,5,6,7,8,9]

f=list(map(squareit,l))
print(f)




from functools import reduce

def add(a,b):
    return a+b

l=[1,2,3,4,5,6,7,8,9]

f=reduce(add,l)
print(f)








# ===================================================================================================================


# Decorator Function ---
            #  decorator is a function which can take a function as an argument and
            # extend its functionality and returns modified function with extended functionality




def decor(func):

    def inner():
        print("Decorator with extra feature")
        print("All possible decorator")
        func()
    return inner

@decor
def f1():
    print("showing sunny")

f1()
f1()




def decor1(func):
    def inner():
        print("Enhanced function")
        func()                   # calling f()
    return inner

@decor1
def f():
    print("Original function")

f()





def sunny_decor(f1):
    def inner(name):
        if name=='sunny':
            print(name,"you are great")
        else:
            f1(name)
    return inner


@sunny_decor
def wish(name):
    print("hello",name,"good evening")

wish('jay')
wish('ravi')







def decor_add_function(x):
    def inner(a,b):
        print("Adding two number function ")
        print("First argument:",a)
        print("Second argument:",b)
        print('The sum of {} and {} is : {}'.format(a,b,a+b))
        # print('The sum of ',a,' and ',b,' is :',a+b)
    return inner

@decor_add_function
def add(a,b):
    print(a+b)

# add(10,30)
# add(20,40)
# add(100,200)

enhanced_decor=decor_add_function(add)
add(50,60)




def smart_division(func):
    def inner(a,b):
        print('We are dividing {} with {}'.format(a,b))
        if b==0:
            print('can`t divide with 0.')
            return
        else:
            return func(a,b)
    return inner


@smart_division
def division(a,b):
    return a/b

print(division(20,3))
print(division(20,0))








def decor2(func):
    def inner2():
        print("Decor 2 enhanced function")
        func()
    return inner2

def decor1(func):
    def inner1():
        print("Decor 1 enhanced function")
        func()
    return inner1

@decor2
@decor1
def f1():
    print("original function")

f1()  # decor 2 function


@decor1
@decor2
def f1():
    print("original function")

f1()  # decor 1 function









def decor1(func):
    def inner1():
        x=func()
        return x*x
    return inner1

def decor2(func):
    def inner2():
        x=func()
        return 2*x
    return inner2

@decor1
@decor2
def num():
    return 10

print(num())



@decor2
@decor1
def num():
    return 10

print(num())








# class Test:
#     @staticmethod
#     def f1():pass
#
#
# @login_required
# def view_function(): pass








# ------------------------------------------------------------------------------------------------------
# ques --

# WAP to generate fake employee data for database operation ?

# ---------------------------------------------------
# Employee Name : Dsdjbvunci( exactly 3 to 10 character)
# Employee Number: e-1234 ,....
# Employee Salary: 10000 to 50000
# Employee City : Madras
# Mobile Number: 6 to 9
# Designation:
#              Software Engineer
#              Senior Software Engineer
#              Team Lead
#              Project Lead
#              Manager Lead




import random
import string

# List of cities
cities = [
    "Madras", "Delhi", "Mumbai", "Pune",
    "Hyderabad", "Bangalore", "Kolkata", "Chennai"
]

# List of designations
designations = [
    "Software Engineer",
    "Senior Software Engineer",
    "Team Lead",
    "Project Lead",
    "Manager Lead"
]

# Generate random employee name (3 to 10 letters)
def generate_name():
    length = random.randint(3, 10)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Generate employee number (E-1234)
def generate_emp_number():
    return f"E-{random.randint(1000, 9999)}"

# Generate salary (10000 to 50000)
def generate_salary():
    return random.randint(10000, 50000)

# Generate mobile number (starts with 6 to 9)
def generate_mobile():
    first_digit = str(random.randint(6, 9))
    remaining = ''.join(random.choice(string.digits) for _ in range(9))
    return first_digit + remaining

# Generate one employee record
def generate_employee():
    employee = {
        "Employee Name": generate_name(),
        "Employee Number": generate_emp_number(),
        "Employee Salary": generate_salary(),
        "Employee City": random.choice(cities),
        "Mobile Number": generate_mobile(),
        "Designation": random.choice(designations)
    }
    return employee

# Generate 5 fake employees
for i in range(5):
    emp = generate_employee()
    print(f"\nEmployee {i+1}")
    print("-" * 30)
    for key, value in emp.items():
        print(f"{key:18}: {value}")



