# string method for remove spaces
# lstrip() ---> remove space from left
# rstrip() --> remove space from right
# strip()--> remove space from both side

s= "   jay   "
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# ------------------------------------------------------------------
# finding substring in string
# find() ---> to check substring(index) is available or not
# index()---->

# ------------------------------------------------------------------
# find() ----> forward find -----------------
# rfind() --> reverse find-----------
s="learning ear python"
print(s.find("ing"))
print(s.find("jay")) # not available so return -1
print(s.rfind("ea"))
print(s.rfind("py"))
print(s.find(" "))
print(s.find("ea",5,15))



#--------------------------------------------------------------------------------------
# index()----> forward find ,--------------------------------------
#  if the substring is not available the it will give value error
s= "i am playing with python"
print(s.index("ing"))
print(s.index("ing",5,15))
# print(s.index("jay",5,15)) # error

s=input("Enter the main string:")
substr=input("Enter the substring :")
try:
    n=s.index(substr)
    print("substring found at index:", n)
except ValueError :
    print("substring not found.")
else:
    print("substring found at index:",n)


# ---------------------------------------------------------------------------------------
# WAP to display all position of substring in the given main string
s=input("Enter main string:")
subs=input("enter substring:")
flag=False
pos=-1  # position
n=len(s)
count=0
while True:
    pos=s.find(subs,pos+1,n)
    if pos ==-1:
        break
    print("substring found at index:",pos)
    flag=True
    count+=1
if flag==False:
    print("substring not found.")
print("how many times substring found:",count)


# --------------------------------------------------------------------------------
#  count() ------> count the string character
s='jayvardhansingh'
print(s.count('a')) # total string
print(s.count('a',5,10))
print(s.count('a',4,len(s)))



# ----------------------------------------------------------------------------------------
#  replace() ----->  replace the string with another string
#  create a new object while replacing the string in memory
s= " learning python is not good"
print(s)
s1=s.replace("not","very")
print(s1)
print(s.replace("python","java"))

print(s,"address is:",id(s))
print(s1,"address is:",id(s1))


# ----------------------------------------------------------------------
# split() --- splitting of string in list --------
s= " learning-python-is-not good"
print(s.split())
s1= s.split("-")
print(s1)
print(type(s1)) #  list type
for i in s1:
    print(i)

# rsplit() --------------------------------------
s= " learning python is not good"
print(s.split(' ',3))
print(s.rsplit(' ',3))


s="1,2,3,45,5,6,7,8,9"
l=s.split(',',3)
print(l)
l=s.rsplit(',',3)
print(l)



# ---------------------------------------------------------------------------------
# join()  --> join the strings
l=[' learning python', 'is', 'not', 'good']
s='-'.join(l)
print(s)
print(''.join(l))

tuple1=(' learning python', 'is', 'not', 'good')
s='--'.join(tuple1)
print(s)


#-------------------------------------------------------------------
# changing case of string -----------

# upper() ----> convert to upper case -----------------------
# lower() ----> convert to lower case -----------------------------
# swapcase() ----> stap the case --------------------
# title() ----> evey word start with upper case ----------Convert In The Title Case
# capitalize() ----> in the total string only first character is upper case ---------

s="learning Python is good"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())



# -------------------------------------------------------------------------------
# checking starting and ending part of the string
# startswith() ---> check the start part of the string
# endswith() --> check the end part of str

s="learning Python is good"
print(s.startswith("learning"))
print(s.startswith("python"))
print(s.endswith("good"))
print(s.endswith("is"))
print(s.startswith("learning",5,15))



# -------------------------------------------------------------------
# isalnum() ---> is alpha numerical --> string contain only alphanumeric character a-z, A-Z , 0-9
# isalpha()
# isdigit()
# islower()
# isupper()
# istitle()
# isspace()
# isnumeric()

print('jay123'.isalnum()) # true
print('jay123'.isalpha()) # false
print('jay'.isalpha())    #true
print('jay123'.isdigit()) # false
print('123'.isdigit()) # true
print('jay'.islower()) # true
print('ABC'.islower()) # false
print('jay123'.islower())  # true
print('jay'.isupper()) # false
print('ABC'.isupper())  # true
print('learning python is easy'.istitle()) # false
print('Learning Python Is Easy'.istitle()) # true
print('  '.isspace()) # true
print(''.isspace()) # false
print('jay vardhan '.isspace()) # false
print('A123'.istitle()) # true



s=input("enter any character:")
if s.isalnum():
    print("Alpha Numeric Character.")
    if s.isalpha():
        print("Alpha character.")
        if s.islower():
            print("Lower case alphabet character. ")
        else:
            print("Upper case alphabet character.")
    else:
        print("Digit character.")
elif s.isspace():
    print("Space character.")
else:
    print("Special character.")




# -------------------------------------------------------------------------------------
# Formatting string concept
# format() ----> use to format the string---------------------------

name="Jay"
age=40
salary=10000
print(" {} age is {} and salary is {}".format(name,age,salary))
print(" {0} age is {1} and salary is {2}".format(name,age,salary))
print(" {A} age is {B} and salary is {C}".format(A=name,B=age,C=salary))
print( name,"age is",age,"and salary is",salary)



# ------------------------------------------------------------------------
#  WAP to reverse the given string
s=input("Enter string:")
print(s[::-1])   # first method

for i in range(len(s)-1,-1,-1):  # second method
    print(s[i],end='')
print()
print(reversed(s)) # third method
for i in reversed(s):
    print(i,end='',)
print()
print(''.join(reversed(s)))

i=len(s)-1
output=''
while i>=0:
    output=output+ s[i]
    i=i-1
    # print(output)
print(output)


#  WAP to reverse the given string order but not reverse the character
s=input("Enter string:")
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i-=1
print(l1)
print(' '.join(l1))


# ---------------------------------------------------------------------------------------
# wap to reverse words character------
s=input("Enter string:")
l=s.split()
l1=[]
for i in l:
    l1.append(i[::-1])
    # print(l1)
print(l1)
print(' '.join(l1))


# ---------------------------------------------------------------------------------------
#  input --> S1=RAVISOFT
#            S2=TEJA
# output --> RTAEVJIASOFT

s1=input("Enter first string:")
s2=input("Enter second string:")
output=''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)




# ---------------------------------------------------------------------------------------
#  input --> B4A1D3
# output --> ABD134

s = input("Enter string:")
s1=s2=output=""
for i in s:
    if i.isalpha():
        s1=s1+i
    elif i.isdigit():
    # else:
        s2=s2+i
print(s1)
print(s2)
print(s1+s2)

for i in sorted(s1):
    output=output+i
for i in sorted(s2):
    output=output+i
print(output)


# output=s1+s2    # not much correct
# print(sorted(output))



# ---------------------------------------------------------------------------------------
#  input --> a4b3
# output --> aaaa4444bbbb3333

s = input("Enter string:")
output=""
for i in s:
    if i.isalpha():
        output=output+i
        previous=i
    else:
        output=output+ previous * (int(i)-1)

print(output)




# ---------------------------------------------------------------------------------------
#  input --> a4k3b2
# output --> aeknbd


print(chr(97))  # unicode value to character
print(chr(98))
print(chr(99))

s=input("Enter some string:")
output=""
for i in s:
    if i.isalpha():
        output=output+i
        previous=i
    else:
        newchar=chr(ord(previous)+int(i))
        output=output+newchar
print(output)


# -----------------------------------------------------------------------------
# Wap to print character is present at odd or even
s=input("Enter string:")
print("Character at Even position",s[::2])
print("Character at odd position",s[1::2])

i=0
print("Character at Even position:")
while i<len(s):
    print(s[i],end=',')
    i+=2
print()
i=1
print("Character at odd position:")
while i<len(s):
    print(s[i],end=',')
    i+=2




# --------------------------------------------------------------------------------------------------------
#  WAP to remove duplicates from string
s=input("Enter string:")
print(''.join (set(s)))


output=''   # first method
for i in s:
    if i not in output:
        output=output+i
print(output)

l=[]   # second method
for i in s:
    if i not in l:
        l.append(i)
output=''.join(l)
print(output)
print(''.join(l))



# -------------------------------------------------------------------------
# WAP to find the number of occurrences of character in string
s=input("Enter the string:")
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)


for i in s:
    if i not in d.keys():
        d[i]+1
    else:
        d[i]=d[i]+1
print(d)

for k,v in d.items():
    print(f"{k} == {v}")




#
# Reverse a string in Python.
#
# Check if a string is palindrome.
#
# Count vowels and consonants in a string.
#
# Count frequency of each character in a string.
#
# Find duplicate characters in a string.
#
# Remove duplicate characters from a string.
#
# Check if two strings are anagrams.
#
# Find first non-repeating character.
#
# Find longest word in a string.
#
# Count number of words in a sentence.
#
# Convert string to integer without using int().
#
# Remove spaces from a string.
#
# Replace spaces with special character (like _).
#
# Check if a string contains only digits.
#
# Count uppercase and lowercase letters.
#
# Convert first letter of every word into uppercase.
#
# Sort characters of a string alphabetically.
#
# Find substring occurrence count.
#
# Check if one string is rotation of another.
#
# 6. Advanced String Concepts
#
# Explain immutability of strings and its impact on memory.
#
# What is id() in strings?
#
# What is string interning in Python?
#
# Difference between == and is in strings.
#
# What is Unicode in Python strings?
#
# Explain ASCII vs Unicode.
#
# How does Python store strings internally?
#
# Time complexity of string concatenation using +.
#

