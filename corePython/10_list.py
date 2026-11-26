# List Data Structure --------------------------------------------------------
# mutable , [] ,
# group of value where insertion order is preserved
# and duplicates are allowed
# index --  +ve and -ve


# 1. Empty list  -----------------------------
l=[]

l=[10,20,30,40,50,'jay',True]
print(l)
print(type(l))

# 2. Dynamic list -------------------------------
l=eval(input("Enter the list:"))
print(l)

# 3. List function -------------------------------------
s="jay vardhan singh"
l=list(s)
print(l)

# 4. split() function ---------------------------------------
s="jay vardhan singh"
l=s.split()
print(l)
print(s.split())

# 5. Nested list ---------------------------------
# list inside a list is called as the nested list
l=[1,2,[3,4],5,6,[7,8],9]


# ----------------------------------------------------------
# 6. Accessing the list elements
#  index ---------------------------
#  slice ------------------------

l=[10,20,[30,40],50,'jay',True]

print(l[0])
print(l[-1])
for i in l:
    print(i)
print(l[2][0])


print(l[::])#[10, 20, [30, 40], 50, 'jay', True]
print(l[::2])#[10, [30, 40], 'jay']
print(l[::-1])#[True, 'jay', 50, [30, 40], 20, 10]
print(l[0:3])#[10, 20, [30, 40]]




# --------------------------------------------------
# list vs immutable -------------------------------------------------

l=[10,20,3,50]
l[1]=90
print(l)

i=0
while i<len(l):
    print(l[i])
    i=i+1

for i in l:
    print(i)

for i in l:
    if i%2==0:
        print(i)


list=['a','b','c','d','e']
i=len(list)
for j in range(i):
    print(list[j],f"is available at positive index: {j} and negative index {j-i}")




#  --------------------------------------------------------------------------
#  Important list functions --------------
# methods -- function declared inside the class called method
# functions  -- functions declared outside the class
def f1():
    print("hello this is function")
class student:
    def info (self):
        print("hello this is a method:")
f1()  # function
s=student()  # method
s.info()

# -----------------------------------------------------------
# 1. len() function --- get the length of the list
# 2. count() ---- number of occurrences of each character
# 3. index() --- to get the index

list=[10,20,30,50,60,70]
print(list.count(10))
print(len(list))
print(list.index(30)) # to get the index
# print(list.index('z')) # value error


target=int(input("Enter the value to search:"))
if target in list:
    print(target," available and its occurrence is at index",list.index(target))
else:
    print(target," not available")


# --------------------------------------------------------------------------------------------
# Manipulating elements of list -----------------------------------------
# ----------------------------------
# 4. append() -- to add the value to the list

l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)

# WAP to add all elements to list upto 100 which are divisible by 10

l=[]
i=0
while i<=100:
    if i%10==0:
        l.append(i)
    i+=1
print(l)

for i in range(0,101,10):
     print(i)
print(l)

for i in range(101):
    if i%10==0:
        l.append(i)
print(l)

# ---------------------------------------------
# 5.insert --- to insert the value to the list in a specific index

l=[]
l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)

l.insert(1,50)
print(l)
l.insert(30,70)
print(l)



# ---------------------------------------
# 6. extend() -- to add multiple values to the list

l1=['chiken','fish']
l2=['kf','rc','fg']
l3=l1+l2

l1.extend(l2)
print(l2)
print(l1)
print(l3)

l1.extend('jay')
print(l1)


# --------------------------------------------------------
# 7. remove() ---- to remove the specified element from the list

list=[10,20,30,50,60,70]
list.remove(30)
print(list)

x=int(input("Enter element to remove:"))

if x in list:
    list.remove(x)
    print("Element is removed")
    print(list)
else:
    print("Element is not available.")

# --------------------------------------------------------------
# 8.  pop() --- to remove the last element from the list

list=[10,20,30,50,60,70]
list.pop()
print(list)

print(list.pop(2))
print(list)


# -------------------------------------
# clear() --- do clear whole list

list=[10,20,30,50,60,70]
list.clear()
print(list)


# ---------------------------------------------------------
# Ordering elements of the list --------------
# --------------------------
# 9. reverse() -- to reverse the list

list=[10,20,30,50,60,70]
list.reverse()
print(list)

# --------------------------------------------------------
# 10. sort() -- to sort the element of the list

list=[10,20,50,80,25,70]
list.sort()
print(list)

l=['dog','apple','cat']
l.sort()
print(l)

list=['10','20','30','dog','apple','cat']
list.sort()
print(list)

# for Descending order
list.sort(reverse=True)
print(list)


# --------------------------------------------------
# 10.  copy methods ---------
# --------------------------------------------
# shallow copy or alias
x=[10,20,50,80,25,70]
y=x # shallow copy
print(id(x))
print(id(y))
y[1]=100
print(x)

# -------------------------------------------------------
# deep copy -->  .copy() --------------------

x=[10,20,50,80,25,70]
# y=x[:] # deep copy
y=x.copy() # deep copy or cloning
print(id(x))
print(id(y))
y[1]=100
print(x)
print(y)



# ----------------------------------------------------------
#  mathematical operators  -----------------------------

#  +   ------------
a=[1,2,3,4]
b=[5,6,7,8,9]
c=a+b
print(c)
c=a+[40]
print(c)

# * --------------
c=a*3
print(c)


# -------------------------------------------------
# Comparison of list --------------------

x=['Dog','Cat','Rat']
y=['Dog','Cat','Rat']
z=['DOG','CAT','RAT']
print(x==y) # true
print(x==z) # false
print(z==y) # false

print(x is y) # false --> id comparison
print(x is z) # false
print(x[0] is y[0]) # true
print(id(x[0]))
print(id(y[0]))



x=[50,20,30]
y=[40,90,100,120]
print(x>y)  # compare only first element
print(x[0] > y[0])

x=['Dog','Cat','Rat']
y=['Rat','Cat','Rat']
print(x>y)  # compare only first character of first element
print(x[0] > y[0])

x=[50,20,30]
print(10 in  x)
print(100 in x)
print(10 not in x)
print(40 not in x)

# ----------------------------------------------------------------------
# Nested list --- list inside list

x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
for i in x:
    print(i)

print("Elements in matrix style:")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=' ')
    print()
print()

print("using while loop:")
i=0
while i<len(x):
    j=0
    while j<len(x[i]):
        print(x[i][j],end=' ')
        j=j+1
    print()
    i=i+1



# -----------------------------------------------------------
#  List comprehension ----------------------
# list=[expression for item in sequence] --------


# l1=[]
# for i in range(1,11):
#     l1.append(i)
# print(l1)

l=[i*i for i in range(1,11)]  # list comprehension
print(l)

# even numbers
l1=[i*i for i in range(1,11)]
l2=[i for i in l1 if i%2==0]
print(l2)

# odd numbers
l1=[i*i for i in range(1,11)]
l2=[i for i in l1 if i%2!=0]
print(l2)

l1=[2**i for i in range(1,11)]
print(l1)


# print the first character ----------------------
words=['Bhavani','nag','venkatesh','rajni']
l=[w[0] for w in words ]
print(l)

l=[w for w in words if len(w)>5]
print(l)


n1=[10,20,30,40]
n2=[30,40,50,60]
n3=[i for i in n1 if i not in n2]
print(n3)

words="the quick brown fox jumps over the lazy dog".split()  # convert string to list
print(words)

l=[w.upper() for w in words] # to upper case
print(l)

l=[[w.upper(),len(w)] for w in words] # to upper case
print(l)



# ------------------------------------------------------------------
# whole A to Z alphabets in a sentence

# the quick brown fox jumps over the lazy dog


# --------------------------------------------------------------------
# WAP to display unique vowels present in the given word

word=input("Enter word:")
vowels=['a','e','i','o','u','A','E','I','O','U']
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            # print(letter)
            found.append(letter)
print(found)
print("The number of different vowels present in ",word,"is",len(found))



l1=[10,20,30,25,5]
print(l1)
l1.insert(3,50)
print(l)

