# module -- a group of variables and functions saved in a file is module
# code reusability , readability , maintainability



x=88
y=99
def add (a,b):
    print("the sum is:",(a+b))

def sub (a,b):
    print("the sum is:",(a-b))

def product(a,b):
    print("the product is:",a*b)

def division(a,b):
    print("the product is:", a / b)

# add(10,20)
# sub(10,20)
# division(10,20)
# product(10,20)



# -----------------------------------------------
# print("This is module 1.....")
# print("hii")

# --------------------------------------------
def f1():
    print("this is from module 1.....")
    if __name__=='__main__':
        print("the code executed directly as program")
        print("the value of __name__",__name__)
    else:
        print("the code executed indirectly as a module from some other program")
        print("the value of __name__:", __name__)
f1()






