# module =====>
# a group of functions, variables, classes
# Libraries =====> a group of modules
#
# math module ----------------------
import math
print(math.sqrt(16))
print(math.pi)

#  aliasing ---------- to change the module name
import math as m
print(m.sqrt(25))
print(m.pi)



from math import sqrt , pi
print(sqrt(25))
print(pi)


from math import *
print(sqrt(25))
print(pi)


#  math functions
# sqrt()
# ceil()
# floor()
# pow(x,y)
# factorial()
# gcd()
# sin()
# cos()



#  area of circle------------------------
from math import *
r=eval(input(" Enter radius:"))
area=pi*r**2
print("the area of circle is: ",area)


