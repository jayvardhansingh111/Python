# set ------ instruction order is not preserved,duplicates are not allowed
#  , mutable, {}

# diff between list and set ------------------------------
# in  the list duplicates are allowed and in set duplicates are not allowed ,

s={10,20,30,40,50,60}
print(type(s))
# print(s[0]) #TypeError: 'set' object is not subscriptable
print(s)
print(s)

# -----------------------------------------------------------------------------------
# we can also convert any other type to set type by the use of set()
# s=set(any sequence)

s=set('jay')
print(s)
s=set(range(1,6))
print(s)

l=[1,2,3,4,5,6]
s=set(l)
print(s)


s=set() # for create empty set
print(type(s))

# ----------------------------------------------------------------
# important functions of set ----
# ------------------------------------
# add()--- to add a new element to the set -- only one element
s={1,2,3,4}
s.add(10)
s.add(20)
s.add(30)
s.add(40)
print(s)
s.add('jay')
print(s)

# ---------------------------------------------
# update() -- to update the element or group of element to the set
s.update()
l=[9,7,6]
s.update(l) # any number of argument we can pass
print(s)
s.update(l,range(1,5),'jay')
print(s)
s.update('jay'+'vardhan')
print(s)

# -----------------------------------------
# copy() --- cloning -- for different copy of object

s={1,2,3,4}
s1=s.copy()
print(id(s))
print(id(s1))


# -----------------------------------------------
# pop()--- for remove random element ,
s={10,20,30,40,50}
s.pop()
print(s)
print(s.pop())
print(s.pop())

# --------------------------------------------------
# remove()--- to remove specific element
s={10,20,30,40,50}
s.remove(20)
print(s)
# s.remove(120) # if not have that value then through the error
print(s)

# -----------------------------------------
# discard() --- if element not available then no error it ignores that error
s={10,20,30,40,50}
s.discard(120)
print(s)
s.discard(20)
print(s)


# -----------------------------------------------
# clear()--- to remove all the element
s={10,20,30,40,50}
s.clear()
print(s)

# ------------------------------------------------------------------------
# Mathematical operations --------------------------
# ---------------------------------------------
# union()--or |  --- all the element from both set

s={10,20,30,40,50}
s1={60,70,80,90}
print(s.union(s1))
print(s|s1)
# ---------------------------------------
# intersection() or & = --- common element from both set
s={10,20,30,40,50}
s1={50,60,70,80,90}
print(s.intersection(s1))
print(s & s1)

# -----------------------------------------------
# difference() or -    --- to find the difference from both the set
s={10,20,30,40,50}
s1={10,20,60,70,80,90}
print(s.difference(s1))
print(s - s1)

# ----------------------------------------
# symmetric_difference() or ^ --------- nor give the common element

s={10,20,30,40,50}
s1={10,20,60,70,80,90}
print(s.symmetric_difference(s1))
print(s ^ s1)


# ---------------------------------------------
s=set('jay')
print(s)
print('a' in s)
print('d' in s)


# ---------------------------------------------------
# set comprehension -------------
s={x*x for x in range(1,6)}
print(s)
s={x*x for x in range(1,6) if x%2==0}
print(s)

# ---------------------------------------
# indexing and slicing is not applicable

# -------------------------------------------------------
#  WAP to eliminate duplicates present in the list
l=eval(input("Enter some list of value:"))
s=set(l)
print(s)
l1=[]
for x in l:
    if x not  in l1:
        l1.append(x)
print(l1)

# -----------------------------------------------
# to find the vowel in the string
w=input("Enter any word:")
s=set(w)
v={'a','e','i','o','u','A','E','I','O','U'}
d=s.intersection(v)
print("the different vowel present in given word:",d)
print("the number of different vowel:",len(d))

