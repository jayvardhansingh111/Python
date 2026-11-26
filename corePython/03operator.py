 # operators

# 1. Arithmetic
# 2. Relational or Comparison
# 3.  Logical
# 4. Bitwise
# 5. Assignment
# 6 Special
#

# 1. Arithmetic ===========================> there is 7 Arithmetic operators ============================================
a=10
b=2

#  +  ===> Addition  ===> also applicable for str type ==> string concatenation operator
print("a+b: ",a+b)
print('jay'+'3')
print('jay'+str(3))

#  -  ========> Subtraction
print("a-b: ",a-b)

#  * ========> Multiplication == for str it is string multiplication operator
print("a*b: ",a*b)
print('jay'*3)
# print('jay'*'3') # error === one argument should be number

#  /  ==> Division #   === float
print("a/b: ",a/b)

#  % ==> Modulo
print("a%b: ",a%b)

# // ==> Floor Division   === int or float
print("a//b: ",a//b)
print(10//3)
print(10.0//3)

#  **  ==> power or Exponent
print("a**b: ",a**b)
print(10** -2)
print((10+2j)**(10+3j))


a=10.5
b=2
print("a/b: ",a/b)
print("a//b: ",a//b)



# 2. Relational or Comparison   =================================================
# <, >, ,>= , <=    ---- also applicable on string

a=10
b=20
print("a<b :",a<b)
print("a>b :",a>b)
print("a<=b :",a<=b)
print("a>=b :",a>=b)

#  for string , Unicode value is == A = 65 , a=97
a="durga"
b="dame"
print("a<b :",a<b)
print("a>b :",a>b)
print("a<=b :",a<=b)
print("a>=b :",a>=b)

a=True
b=False
print("a<b :",a<b)
print("a>b :",a>b)
print("a<=b :",a<=b)
print("a>=b :",a>=b)

a=10
b=20
if (a>b):
    print("a is grater then b")
else:
    print("a is not grater then b")


#  Chaining of relational operator  ----------------------
print(10<20<30<40)
print(10<20<30>40)  # one is false then answer is false
print(10<20<30<50>40)

# Equality operator  -----------------------------------------
#  ==  ,  !=
print(10==20)
print(False==False)
print('jay'=='jay')
print(10=='jay')
print(10==20==30)
print(10==2*5==3+7)
print((10+2j)==(10+2j))
print((10+2j)=='jay')
print(10==10.0)
print(10==10.1)
print(10=='10')   # false
print(1==True)

print(10!=20)





# 3.   Logical  ====================================================================
#  and , or ,not

# boolean  -------------------
# and ==>  if both arguments are true then only true
# or  ==> if at least one arguments is true then true
# not ==> not true

#  For non-boolean types --------------
# 0 means False
# nin zero means True
# empty string ==> False

#   x and y ------------------------
#  if x evaluates to false then result is x otherwise returns y
print(10 and 20) # ---20
print(0 and 20) # --- 0
print(1 and 'jay')
print(0 and 'jay')

#  x or y  -----------------------------
# if x evaluates to true then returns x otherwise returns y
print(10 or 20)
print(0 or 20)
print(0 or 0)

#  not x ------------------------------
print(not 10)
print(not '')
print(not 0)




# 4. Bitwise operator ==================================================================
#  applicable only int and boolean
#  & -- and  ---> if both bits are 1 then only 1 otherwise 0
#  | -- or  ---> if at least one bit id 1 then 1 otherwise 0
#  ^ -- x-or --> if both bits are different then 1 otherwise 0
#  ~ -- bitwise complement ---> it gives complement of bits [ if 1 then 0 , 0 then 1]
#  << -- bitwise left shift
#  >> -- bitwise right sift

print(4&5)
print(4|5)
print(~4)  #  -5
print(~True)
print(10<<2)
print(10>>2)
print(True<<2)
print(True>>2)





# 5. Assignment ==================================================
#  Assignment operator(=)
x=10
a,b,c,d,= 10,20,30,40

#  compound assignment operator -----------------------------------
#  += , -+ , *= , /= , %= . //= , **= , &= , |= , ^= , >>= , <<=
x=20
x += 10  # x= x+10
print(x)
a=4
a &= 5
print(a)

# ----------------------------------------------------------------------------------
#  Ternary operator  --------------------------------------------
# x=firstValue if (condition) else secondValue
x=30 if (10<20) else 40
print(x)

a,b=10,20
x=30 if (a>b) else 40
print(x)

a=eval(input("Enter first nuber "))
b=eval(input("Enter second nuber "))
min=a if a<b else b
print('minimum value is :',min)

x=10 if 20<30 else 40 if 50<60 else 70
print(x)
x=10 if 20>30 else 40 if 50>60 else 70
print(x)

a=eval(input("Enter first nuber "))
b=eval(input("Enter second nuber "))
c=eval(input("Enter third nuber "))
max=a if a>b and a>c else b if b>c else c
print('maximum value is :',max)

a=eval(input("Enter first nuber "))
b=eval(input("Enter second nuber "))
print('equal' if a==b else ' first greater' if a>b else ' first smaller' )


 # ++  --->  there is no concept of increment and decrement operators in python
# print(++x)
# print(x++)
# print(--x)
# print(x--)




# --------------------------------------------------------------------------------------------
# 6. Special  ===================================================

#  Identity operator --- point to the same address of the variable where the data is stored
#  is , is not  --------
a=10
b=10
c=20
print(a is b)
print(a is not b)
print(a is c)
print(a is not c)
print(id(a))
print(id(b))
print(id(c))

list1=[1,2,3]
list2=[1,2,3]
print(id(list1))
print(id(list2))
print( list1 is list2) # address comparison
print(list1 == list2) # content comparison


 # --------------------------------------------------------------------------------------
 # Membership operator ------------------------------------------------
#  in , not in
list1=[1,2,3]
print(1 in list1)
print(10 not in list1)
print( 1 not in list1)

s=" Hello, i am  Learning Python "
print("p" in s)
print("h" not in s)
print("j" not in s)
print("s" in s)
print('python' in s)
print('jay' in s)




# -------------------------------------------------------------------------------------
#  operator precedence ----------===================================
# () ---> highest precedence
# **  ----->exponential operator
# ~ , -->  unary operator
# *, /,%,//
# +,-
# << , >>
# &
# ^
# |
# >,>=,<,<=,==,!=
#  = , +=,-=,*=
# is , is not
# in , not in
# not
# and
# or


a=30
b=20
c=10
d=5
print((a+b)*c/d)
print((a+b)*(c/d))
print(a+(b*c)/d)




