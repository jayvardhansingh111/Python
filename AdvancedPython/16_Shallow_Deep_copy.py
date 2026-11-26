l1=[10,20,30]
l2=l1          # aliasing -- giving the reference
l2[1]=90
print(l1)
print(l2)


l1=[10,20,30]
l2=l1.copy()  # copying the object
l2[1]=90
print(l1)
print(l2)


# -------------------------------------------------------------------------------
# copy -- the process of copying the exact object

# Shallow copy -     A shallow copy creates a new object, but does not create copies of nested objects.
# Instead, both the original and copied object share the same nested objects.

import copy
l1=[10,20,30,[40,50],60]
l2=copy.copy(l1)

print(id(l1[2]))
print(id(l2[2]))
print(id(l1))
print(id(l2))

l2[3][0]=888
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l2[2]=999
print(l1)
print(l2)
print(id(l1))
print(id(l2))



print(id(l1[2]))
print(id(l2[2]))




# -------------------------------------------------------------------------------
# 2. Deep Copy ---

# A deep copy creates a completely independent copy of the object
# including all nested objects.


import copy
l1=[10,20,30,[40,50],60]
l2=copy.deepcopy(l1)

print(id(l1[2]))
print(id(l2[2]))
print(id(l1))
print(id(l2))

l2[3][0]=888
print(l1)
print(l2)
print(id(l1))
print(id(l2))
print(id(l1[2]))
print(id(l2[2]))



l1=[10,20,30,[40,50],60]
l2=l1.copy()                # shallow copy

print(id(l1[2]))
print(id(l2[2]))
print(id(l1))
print(id(l2))

l2[3][0]=888
print(l1)
print(l2)

print(id(l1[2]))
print(id(l2[2]))






# ---------------------------------------------------------
#
# 1.  if original object does not contain any nested objects then we should go for shallow copy
#
# 2.  if original object contains any nested object then we should go for the deep copy

