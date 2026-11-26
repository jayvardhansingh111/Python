# tuple =====> immutable , (), group of values
#  read only version of list is : tuple

# () - are not mandatory for assigning tuple

tuple1=10,20,30,40,50
tuple2=(10,20,30,40,50,True,'jay',10,20)
print(tuple1)
print(type(tuple1))


# ----------------------------------------------
t=(10)
print(type(t)) # int
t=('a')
print(type(t))  #str

# -------------------------------------------------
# single value tuple ----------------------
t=(10,)
t3=10,
print(type(t))
print(type(t3))
t=('a',)
print(type(t))
from itertools import count
from operator import index

# ------------------------------------------------------------------
# tuple() function --> to create tuple , or convert in tuple from other

l=[10,30,40,50]
t=tuple(l)
print(t)
print(t[0])
print(t[1:4:1])
print(t*2)

s='jay'
t=tuple(s)
print(t)
print(t[0])


t=10,20,30,40,50
# t[1]=100 # does not support changes so it is immutable

# =--------------------------------------------------------------------------
# mathematical operator --------------

# +  ,  *
t=10,20,30,40,50

print(t*2)
print(t*3)

t1=('jay','var',10,20)
t3=t1+t
print(t3)


# ---------------------------------------------------------------
#  important function of tuple ------------

# --------------------------------
# length()-- to calculate the length of the tuple
t = (10, 20, 30, 40, 50)
print(len(t))

# ----------------------------------
# count() -- to count the values ,how much present in the tuple
t = (10, 20, 30, 40, 50)
print(t.count(10))

# --------------------------------
# index() -- to access the elements from the index
t = (10, 20, 30, 40, 50)
print(t.index(30))


# -------------------------------------------------------------------
# sorted() --- to sort the values based on the elements

tuple1=(10,20,30,20,40,10,50,True,10,20)

print(sorted(tuple1))
# t=tuple2.sort() # error

t2=tuple(sorted(tuple1))
print(t2)

t2=tuple(sorted(tuple1,reverse=True))
print(t2)


# ---------------------------------------
# min() -- calculate the minimum value
# max() -- calculate the maximum value

t = (10, 20, 30, 40, 50)
print(min(t))
print(max(t))
t='jayA'
print(min(t))
print(max(t))


# ----------------------------------
t1=(40,20,50)
t2=(10,30,60)
print(t1>t2)
print(t1<t2)

# ---------------------------------------

# Tuple packing and tuple unpacking -----
# packing ---- grouping of variables into a single tuple
a=10
b=20
c=30
d=40
t=a,b,c,d  # tuple packing
print(t)
t=[a,b,c,d]  # list
print(t)
t= {a, b, c, d}  # set
print(t)

# unpacking -- to extract the tuple into the variables
t=(10, 20, 30, 40) #tuple
t= {10, 20, 30, 40}
t='jayv'

a,b,c,d=t
print(a)
print(b)
print(c)
print(d)


# -----------------------------------------------------------

# tuple comprehension -- is not supported
t=(x*x for x in range(1,11))
print(t)
for x in t: print(x)
print(type(t))  # <class 'generator'>



# ---------------------------------------------------------
#  wap to take a tuple of numbers from the keyword and print sum ,average

# t=eval(input("Enter some tuple of numbers:"))
# l=len(t)
# sum=0
# for x in t :
#     sum=sum+x
# print("the sum :",sum)
# print("The average ",sum/l)


# -----------------------------------------------
# Difference between list and tuple
#  list is mutable and tuple is immutable

