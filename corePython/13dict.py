# Dictionary Data Structure -----------------
# {}, to holds the key,value pair data
# mutable, order is not there,duplicates can be values not in keys
# empty dictionary -- d=dict()

d={}
d[10]='jay'
d[12]='siva'
d[13]='ravi'
d[5]='ba'
print(d)
print(type(d))

d={'a':'jay','b':'siva','c':'ravi'}
print(d)
print(d['a'])
# print(d['z']) # error

# ----------------------------------------------
# wap to enter the name and % of marks in a dictionary and display info on the screen
records={}
n=eval(input("Enter number of students:"))
i=1
while i<=n:
    name=input("Enter student name:")
    marks=eval(input("enter % of marks:"))
    records[name]=marks
    i=i+1
print("name of student","\t","% of marks")
for x in records:
    print("\t",x,"\t\t\t\t",records[x])


# --------------------------------------------------------
# how to update dictionaries -------
d= {1: 'jay', 2: 'var', 3: 'singh', 4: 'jack'}
d[5]='pavan'
print(d)
d[4]='rahul'
print(d)

# --------------------------------------------------------
# how to delete elements from the dictionaries----
# del    keyword
d= {1: 'jay', 2: 'var', 3: 'singh', 4: 'jack'}
print(d)
del d[1]
print(d)
# del d[8] # error key is not available
del d
# d[7]='boy' # after delete cant access
# print(d)

# -------------------------------
# clear () -- delete all values

d= {1: 'jay', 2: 'var', 3: 'singh', 4: 'jack'}
print(d)
d.clear()
print(d)
d[8]='jj'
print(d)  # after delete we can access


# ----------------------------------------------------------------
# how to assign multiple values for the single key
l=['jay','var','singh']
d={1:l}
print(d)
d={
    1:['jay','var','singh'],
    2:['jay','var','singh']
}
print(d)


# -------------------------------------------------------------------
# important function / methods of dictionary
# --------------------------------
# 1. dict() -- create a dictionary
d=dict([(100,'jay'),(200,'var'),(300,'dha')])# list
print(d)

d=dict(((100,'jay'),(200,'var'),(300,'dha'))) # tuple
print(d)

d=dict({(100, 'jay'), (200, 'var'), (300, 'dha')}) # set
print(d)

# d=dict({[(100, 'jay'), (200, 'var'), (300, 'dha')]}) # error
# print(d)


# --------------------------------
# len() --
d= {1: 'jay', 2: 'var', 3: 'singh', 4: 'jack'}
print(d)
print(len(d))

# -------------------------------------------
# get() -- for get the value
print(d.get(2))
print(d.get(9))
print(d.get(9,'sunny')) # if the value is not available then it provide this
print(d.get(3,'sunny'))

# ----------------------------------------
# pop() -- the corresponding key value removed
print(d)
print(d.pop(3))
print(d)
# ------------------------
# popitem() -- remove randomly value
print(d.popitem())
print(d.popitem())
print(d.popitem())


#-----------------------------------
# keys, values

d=dict(((100,'jay'),(200,'var'),(300,'dha'))) # tuple
print(d)
print(d.keys())
for i in d.keys():
    print(i)

print(d.values())
for i in d.values():
    print(i)


# items ------------------------
d=dict(((100,'jay'),(200,'var'),(300,'dha'))) # tuple
print(d)
print(d.items())
for k,v in d.items():
    print(k,"........",v)

d[9]='jhjh'
print(d)

# -------------------------------------
print(d.setdefault(9,'hb'))
print(d)
print(d.setdefault(7,'djb'))
print(d)

# -----------------------------------
# update()-- update all key values present in the dictionary
# only one argument we can pass

d1={100:'jay',200:'var'}
d2={'a':'apple','b':'banana'}
print(d1)
d1.update(d2)
print(d1)

d3=dict()
# d3.update(d1,d2) # only one argument we can pass
print(d3)

# ----------------------------------------------------------------------------
#  WAP to take dictionary from the keyword and print the sum of values
d=eval(input("enter dictionary:"))
s=sum(d.values())
print("The sum is:",s)

# ------------------------------------------
# WAP to find number of occurrences of each letter in the given string
word=input("Enter some word:")
d={}
for i in word:
    d[i]=d.get(i,0)+1
print(d)
print("sorted:")
print(sorted(d))
for k,v in sorted(d.items()):
    print(k,'occurred....',v,'times')
    # print("{}occurred {} times".format(k,v))


# ---------------------------------
# WAP to find number of vowel present in the string
word=input("enter some word:")
vowels={'a','e','i','o','u','A','E','I','O','U'}
d={}
for i in word:
    if i in vowels:
        d[i]=d.get(i,0)+1
print(d)

for k,v in d.items():
    print("{} occurred {} times".format(k,v))
print(type(d))


# ----------------------------------------------------
# WAP to add student details to the dictionary
n=int(input("enter the number of students:"))
d={}
for i in range(n):
    name=input("Enter students names:")
    marks=eval(input("Enter students marks:"))
    d[name]=marks
print(d)
while True:
    name=input("Enter students name to get marks:")
    marks=d.get(name,-1)
    if marks== -1:
        print("students not found.")
        print("DO You want to add that students then. ")
        option1=input("Enter [yes | no]:")
        if option1=='yes':
            name = input("Enter students names:")
            marks = eval(input("Enter students marks:"))
            d[name] = marks
        print(d)
    else:
        print("The marks of {} : {}".format(name,marks))
    option=input("Do you want to find another students details[yes| no]:")
    if option== "no":
        break
print("\n Thanks for using the application.")



# ------------------------------------------------------
# comprehension ------------------
# key:value
# squares={x:x*x  for i in range(1,7)}

squares={x:x*x for  x in range(1,6)}
print(squares)
doubles={x:2*x for x in range(1,6)}
print(doubles)














