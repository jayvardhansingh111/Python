#  Introduction -------------------------------
#  everything in python is an object
# ------- ----- ---------


x=100
def f1():
  print("hii :",x)
f1()

import math
print(math.sqrt(4))

import random
# print(randint(0,9),randint(0,9),randint(0,9),sep='')
print(random.randint(0,9))


# ----- Identifiers    -------------- -----------------------------------

# Identifiers : a name in python called identifier ===============
#  variable name ,class name, function name
x=10
def f1():
  print(x)
f1()
#
#  Rules to define identifiers ====================================
# 1.-------------------------------------------------
#    alphabet symbol(both upper and lower case)
#    digits(0 to 9)
#    underscore(_)
# 2.----------------------------------------
# identifier should not start with digits
# total=123  ==> valid
# 123total=123 ==> invalid
#
# 3.---------------------------------------------
# identifiers are case sensitive
total=10
print(total)
TOTAL=20
print(TOTAL)

# 4.  -----------------------------
# cant use reserved word
x=10 # ==> valid
# if=2 # ==> invalid

# 5.  ----------------------------------------
# there is no length for identifier
#
#  if identifiers start with
# _ ===> private
# __ ===> strongly private or protected
# __main__ ==> special variable ,language specific identifier




# ---------- Reserved words----------------------------------------------------------------
# reserved words ===== reserved word defines some meaning and functionality
# there are 35 reserved words
import keyword
print(keyword.kwlist)

# True,False,None
# and ,or not,is
# if ,else,elif
# for,while ,break,continue,return,in ,yield
# try,except,finally,raise,assert,async,await
# import,from,as,class,def,pass ,global,nonlocal,lambda,del,with


a=True
print(a)
# b=none  ====> error ==>None
















