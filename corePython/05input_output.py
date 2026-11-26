 #  Input and output statements =========================================================
#
# read dynamic data from the keyword ---------------------------------
#
# python 2. ---------------------------------------
# x=raw_input("Enter some number") #===> # str  ==> requiring typecasting
# y=input("Enter some number")  #====> not requiring typecasting


#  python 3. ---------------------------------
x= input("enter some number")  # =====> str
print(type(x))


x=int(input("enter first num:"))
y=int(input("enter second number:"))
print("the sum:",x+y)

print("the sum:",int(input("enter first num:"))+int(input("enter second num:")))


#  write a program to read data from the keyword eno, eName, eAdd
eno=int(input("Enter emp number:"))
eName=input("Enter name: ")
eSal=float(input("Enter salary :"))
eAddress=input("Enter address:")
married=bool(input("Enter marriage status:[True/ False]"))

print("employee number:",eno)
print("employee name:",eName)
print("employee :",eSal)
print("employee :",eAddress)
print("employee :",married)

print(" :",int(input("enter employee number:")),input("enter name:"))

# --------------------------------------------------------------------------
#  how to read multiple value from the keyword in a single input
a,b=[int(x) for x in input("Enter 2 number:").split() ] # .split()--> uses space between two number
print("The  product is:",a*b)

#  Read two float value from keyword,
a,b=[float(x) for x in input("Enter two float value:").split(',')]
print("The sum:",a+b)

a,b,c,d=[float(x) for x in input("Enter two float value:").split(',')]
print("The sum:",a+b+c+d)

# --------------------------------------------------------------------------------------------------
# eval() => to consider the values data type internally -------------------------------------------

x=eval("10+2+4+5")
y="10+3+23"
print(x)
print(y)


x=int(input("Enter some List")) # here we need eval()
print(type(x))

x=eval(input("Enter some List:")) # here we need eval()
print(type(x))

# =====> we cant use string type input in eval()

a,b,c=[eval(x) for x in input("Enter numbers:").split(',')]
print(type(a))
print(type(b))
print(type(c))





# command line arguments =====================================================================
# -- the arguments which is passes through the command prompt

# argv ==> holds all command line arguments --------------------------------
# argv ===> list type
# sys===> the argv available in sys module

from sys import argv
print(type(argv))  # input ---> #python 05input_output.py 20 30
print(argv)  # output ---> ['05input_output.py', '20', '30']
print(argv[0])
print(argv[1:])
print(argv[1])


import sys
print(sys.argv)
print(sys.argv[0])
print("the number of command line arguments :",len(sys.argv))

for x in argv:
    print(x)
print("slice operator result",argv[1:3])



# read a group of int values from the keyword as cmd line arguments and print them

from sys import argv
args=argv[1:]
sum=0
for x in args:
    n=int(x) # ==== also use eval()
    sum += n
    print(n)
print("the sum:",sum)

print(eval(argv[1])+eval(argv[2]))
print(argv[100])  # error -- index out of range
print(argv[7:100]) # no error because of slicing







# =====================================================================================================

#  output statements  ====> want to print some data to console   --------------------------
# print()    # want to print some data to console ---
#            also use for new line or line seperator
# Form 1.-------------------------------
print("hii")
print()    # line seperator
print("jay")
print("vardhan")
print("hello \n jay")
print("hello\tjay")
print("hello \v jay")

# Form 2.------------------------------------
print("hello"+"jay")
print('jay'*3)
print("jay","vardhan")

# Form 3. -----------------------------------
# print() ===> with variable number of arguments
a,b,c=10,20,30
print("the values are:",a,b,c)

# sep=     -----> seperator attribute------------
print("the values are:",a,b,c,sep=',')
print(10,20,30,40,sep=':',end='....')
print(60,70,80,sep=',')



# print() with end attributes ----------------
# end=   ------ for print the next line data in the same line
print("hello",end=' ')
print("students",end=' ')
print("python",end=' ')
print("very easy",end='')



# print(formatted string)---------------------------------
# %i --> int type
# %d --> int type
# %f --> float
# %s --> str type
# print("formatted string"%(variable list))

a,b,c=10,20,30
print("a value is %i"%a)
print("a value is %i and b value is %i"%(a,b))

name="jay"
l=[1,2,3,4,5,6]
print("hello %s the list is: %s"%(name,l))



# print() function with replacement operator -----------------------------
# {} ==> replacement operator
name="jay"
salary=10000
gf="Anju"
print("Hello {0} your salary is {1} and your gf {2} is waiting".format(name,salary,gf))
print("Hello {} your salary is {} and your gf {} is waiting".format(name,salary,gf))
print("Hello {x} your salary is {y} and your gf {z} is waiting".format(x=name,y=salary,z=gf))


