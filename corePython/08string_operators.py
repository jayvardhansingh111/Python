# string data type ---->  any sequence of character within "" , ''
s='python'
print(type(s))

ch='a'
print(type(ch))

# multiline string literals -----   ''' ''' , """  """
name=""" jay
vardhan
singh"""
print(name)

s="this is 'single quote statement' so there is line"
print(s)
st="this is \"double quote"
print(st)

st="""this is "double' quote"""
print(st)




# --------------------------------------------------------------------------
# how we can access the character in string -----------------------------
# two methods ------------

# 1. indexing ---> by the index of str
# 2. slice operator -->

st="python"
print(st[0])
print(st[-1])


# WAP to access some string from the keyword and print all the character with index ---
st=input("Enter the string:")
n=0
for i in range(len(st)):
    print(f"the character is: {st[i]}:  at positive index: {i} and negative index: {i-len(st)}")
    n+=1

for i in range(len(st)):
    print("the character is: {} at positive index: {} and negative index: {}".format(st[i],i,i-len(st)))
    n+=1



# 2. slice operator in str ----------------------------------------------------------------------
# s[beginIndex:endIndex:step]
# step value can be +ve or -negative


s="0123456789"
print(s[1:7])
print(s[0:6:1])
print(s[0:9:2])
print(s[0:])    # end index is total index in str
print(s[::])
print(s[::-1])  # access right to left index

print(s[2:8:1])  # if +ve forward direction from begin to end-1 ( 2 to 7)
print(s[2:8:-1]) # if -ve backward direction from begin to end+1( empty)
print(s[-1:-6:-1])
print(s[2:-5:1])
print(s[2:-5:-1])





# mathematical operation in string --------------------------------------------------------
#  +  ---> string concatenation --> both value should be string
#  *  ---> one value str and another in int type

s="python"
st="java"
print(s+st)
print("jay"+"vardhan")
# print("jay"+2) # only string can  connect

print("jay "*3)
# print("jay"*3.5) # cant use float

print(len(s))


# WAP to access each character of string in forward and backward direction
s=input("Enter the string:")
# -------------------------------------------------------------------
print("Forward direction:",s[::])
print("backward direction:",s[::-1])
# --------------------------------------------------------------------
print("Forward string:")
for i in range(len(s)):
    # print(f"forward index: {i} and backward index: {len(s)-i} and character is : {s[i]}")
    print(s[i],end='')
print()
print("Backward string:")
for i in range(len(s)):
    print(s[len(s)-i-1],end='')
print()
# ------------------------------------------------------------------------
i=0
print("Forward string:")
while i<len(s):
    print(s[i],end='')
    i+=1
print()
print("backward string:")
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i=i-1
print()
print("again backward string:")
i=-1
while i>= -len(s):
    print(s[i],end='')
    i-=1


# WAP to ----------------------------- -------------------------------
# 1. remove duplicate character from str
# 2. count each character how much time presenting in str
# 3. reverse characters of a words in str








#  membership operator ------------------------
#  in , not in
s="python"
print("y" in s)
print("y" not in s)
print("j" in s)
print("j" not in s)

s=input("Enter string:")
substr=input("Enter substring to find:")
if substr in s:
    print(substr,"found in string")
else:
    print(substr,"not found in string")





# Logical /comparison operators ---> content comparison ---------------------------
# >,<,>=,<=,==,!=   -->  alphabetical order => unicode value
# a=97  ---> unicode
# A=65

s1=input("Enter first string:")
s2=input("Enter second string:")
if s1==s2:
    print("both string have same content.")
elif s1<s2:
    print("first string is smaller then second string.")
else:
    print("first string is bigger then second string.")



# == , is -------------------------
l1=['a','s','d']
l2=['a','s','d']
print(id(l1),id(l2))
print(l1==l2)   # content comparison
print(l1 is l2) # address comparison



city=input("Enter city your name:")
list1=['hyderabad','bangalore','gwalior','pune']
if city.strip() in list1:
    print("your city is listed in this area.")
else:
    print("your city is not listed in this area.")





