# data types ==== represent the type of values
# there is 14 inbuilt datatypes
# int ---- integral value (2,3,4....)
# float ----- decimal value -- 2.4,24.5
# complex -----  2+3j
# bool  ----- True and False
# str   ------- '' , "" , ''' '''
# bytes ----- immutable, 0 to 256 [] ==> binary data
# bytearray ----- mutable [] ==> binary data
# range ----- immutable , sequence of numbers , range()
# list --- mutable , [] ,group of value where insertion order is preserved and duplicates are allowed
# tuple --- immutable , ()
# set ---mutable,{}, duplicates are not allowed, order is not preserved
# frozenset --- immutable ,duplicates are not allowed,order is nor preserved
# dict ----- mutable,key, value === .> {}
# None --- no value associated

#  ==== inbuilt functions==================================================
# 1. print() ==> to print the value
# 2. type()  ==>to check the type of variable
# 3. id()  ==> to get the address of variable



# int ========> for represent the integral value =======================================================
a=20
print(type(a))  #<class 'int'>
# long ==> python 3 has not available

# 1.=> Decimal(base 10)
# 0 to 9

# 2. Binary(0,1)
a=111 # not binary
b=0b11
c=0B11
print(a,b,c)

# 3. Octal(base 8)(0 to 7)
a=0o222
b=0O222
print(a,b)

# 4. Hexa decimal(base 16)(0 to 9 and a to f,A to F)
# (0x,0X)
a=0xFace
b=0X222
print(a,b)

# ========== base conversion in int data type in python
# 1. bin() ==> to convert any base to binary
print(bin(15))
print(bin(0o10))
print(bin(0x10))
# 2. oct() == to convert any base to octal
print(oct(15))
print(oct(0b10))
print(oct(0x10))
# 3. hex() ==> to convert any base to hexa decimal
print(hex(15))
print(hex(0b10))
print(hex(0o10))




# float  =========> for represent the decimal/flot value ================================================
a=10.554
salary=12343.45
price=124.50
print(type(a)) # <class 'float'>

# Exponential form of flot
a=1.2e3 # => 1.2*10^3 ===>
print(a)
b=1.2e100
print(b)




# complex ==========> for complex data type ===============================================
# a+bj => a= real number , b=imaginary number , j=j^2=-1(imaginary)

c=10+20j
print(type(c)) #<class 'float'>
y=10.5+3.4j
print(y)
a=0b11+10j
print(a)

print(a+y)
print(a-y)
print(a*y)
# a=12+0b11j # error => imaginary part cant take conversion values(bin,oct,hex)

a=20+30j
print(a.real)
print(a.imag)



# bool =========>>> for boolean value(Ture,False) =================================================
a=True # True = 1
b=False # False = 0
print(type(a)) # <class 'bool'>
print(a>b)
print(b<b)
print(True+True)
print(True+False)
print(False+False)




#str ==========>> any sequence of characters written in quotes('' , "" ,  ''' ''') ============================

s='hii'
name="jay"
sts='''durga sit"python" classes''' # string literals
LastName='''jay
vardhan
singh
'''
print(type(s))
print(LastName)

# indexing can be possible in string----------
print(s[0])  # left to right
print(s[-3])  # -ve indexing ==> right to left

# =====> slice operator in str=========
# return substring from begin index to end -1
# string[start:end]
s="python"
print(s[0:4])
print(s[2:5])
print(s[1:])
print(s[:5])
print(s[-1:-5]) # provide empty string
print(s[-5:-1]) # provide value

# taking step in str
# s[begin:end:step]=======
s='jayvardhansinghkushwah'
print(s[0:13:2])
print(s[::3])

s="python"
print(s*3) # for repeat the string
print(len(s))

# pythons fundamental data types
# int ,float, complex, bool, str
# these all are immutable

# char ===> is not available only use str





# =====> Type Casting / type coersion in python ============
# int() ===> other to int data type
print(int(10.5))
print(int("10"))
print(int(True))
# print(int(10+2j)) # cant possible


# float() ============== other to float

print(float(10))
print(float("10"))
print(float("10.5"))
# print(float(10+20j)) # cant convert
print(float(True))
print(float(False))
# print(float("hii")) # error
# print(float("0b11")) # error


# complex() ====== other to complex
# form 1 . ---------
print(complex(10))
print(complex(10.5))
print(complex("10"))
print(complex("10.5"))
# print(complex("hii")) # error
print(complex(True))
print(complex(False))

# form 2 . --------
print(complex(20,2))
print(complex(20,2.3))
print(complex(20.3,2))
print(complex(20,2))
print(complex(True,False))
# print(complex("20","2")) # error


# bool() ====== other to bool
print(bool(1))
print(bool(0))
print(bool("10"))
print(bool(''))
print(bool(10.5))
print(bool(10+2j))
print(bool(0))

# str() ====== other to str
print(str(19))
print(str(10.4))
print(str(True))
print(str(False))
print(str(19+10j))


#  immutable ================>> cant change stored id is same
#  all fundamental data types are immutable
#  mutable ===> changeable
v1="hyd"
v2="hyd"
v3="hyd"
v4="gwl"
print(id(v1),id(v2),id(v3))
print(id(v4))
print(v1 is v2)
print(v2 is v3)
print(v1 is v4)

x=256
y=256
print(x is y)

x=257
y=257
print(x is y)

x=10.5
y=10.5
print(x is y)




#bytes ===================>> immutable ===================================================
#  represents a group of bytes numbers , like array
# only except value between 0 to 256
x=[10,20,30,40,50]
b=bytes(x)
print(type(b))
print(b[0])
print(b[-1])
x=[10,20,30,40,255] # only use 0 to 255
# b=bytes(x) # error



# bytearray   ===========> mutable , stores the group of value =======================================
y=[10,20,30,40,50]
b=bytearray(y)
print(type(b))
b[0]=100
for i in b:
    print(i)

x=[10,20,30,40,50]
b=bytearray(x)
# b[1]=258 # cant use only 0 to 155
print(b)



# =================================================================================
#list ===========>>>> mutable , group of value where insertion order is preserved and duplicates are allowed
l=[]
print(type(l))
l.append(10)
l.append(20)
l.append(30)
l.append(20)
l.append(10)
print(l)
l.append('jay')
print(l)
l.append(None)
print(l)
print(l[0])
print(l[-1])
print(l[1:5])  # slicing applied

l.remove(10) # for remove the value
print(l)
s=[10,'jay',True]
print(s*2)
print(type(s))




# tuple ============> immutable , ========================================================
t=(10,20,30,40,50,'jay',True,10,20)
print(type(t))
print(t)
print(t[0])
print(t[-1])
# t[0]=100  # cant change
print(t[1:6:1])
print(t*2)
print(t)
print(t.count(10))
t=(10,20,30,40,50,[1,2,3],60,70)




#range ============>>>>> immutable , sequence of values / numbers =======================
# form 1.--------------
r=range(10)  # 0 to 9
print(type(r))
print(r)
for i in r:
    print(i)

print(r[0])
print(r[0:3])
# r[0]=100 # error

# form 2.-------------------
r=range(10,20) # 10 to 19
print(r)

# form 3. --------------------
r=range(10,30,2)
for i in r:
    print(i)

for i in range(10,30,2):print(i)




# set ====================>> mutable, duplicates are not allowed, order is not preserved =================
s={10,20,30,10,30,}
print(s)
# print(s[0]) # error because order is not applicable
# print(s[0:2]) # error
s.add(14)
s.add('jay')
s.remove(14)
print(s)

s=set()
for i in range(10):
    s.add(i)
print(s)



#
# frozenset ====================> immutable ,duplicates are not allowed,order is nor preserved =================
# group of unique value but no one allow to change
s={10,20,30,10,30,}
fs=frozenset(s)
print(fs)
# fs.add(50) # not allowed
# fs.remove(30) # not allowed




# dict =====================>> mutable,group of key and values ===============================
# key is a unique value and values can be duplicates
dt={1:'jay',
   2:'vardhan',
   3:'singh'
   }
print(dt)
print(dt[1])
dt.update({4:'durga'})
print(dt)
dt[5]='sunny'
dt[2]='rahul' # old value is replaced to the new assign value
print(dt)


# None ===============  no value ===============================================

def f1():
    a=10

def f2():
   print("hello None")
f2()
f1()
print(f1())

def f3():
   amount = int(input('Enter amount: '))
   pass
   if amount>1000:
      print("hhh")
   else:
      pass
f3()




# Escape character ===============================
# \n ===> new line
# \t ----> horizontal tab
# \v ----> vertical tab
# \r ---->
# \b ---> backspace
# \f --
# \'
# \"
# \\

s= "python by \" durga sir\" is good "
s1= 'python by" durga sir" is good'
s2= "python by 'durga sir' is good "
s3= '''' python by "durga sir "is good 'also material' '''
s4="""" python by 'durga sir ' is " good" material also """
s5= ' python by \'durga sir \'is good \"also material\" '
s6=" python by \'durga sir \' is \" good \" material also "



# # constants ==========> fixed value , never ========
# #  there is no concept in python
#
#
#  # use capital letter for not change variable
MAX_VALUE=10









