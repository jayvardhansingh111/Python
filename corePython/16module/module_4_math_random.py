# # math module ------
# import math
# # from math import *
# print(sqrt(4))
# print(ceil(10.1))
# print(floor(10.1))
# print(fabs(-10.6))  # float absolute value
# print(abs(-10))

# print(help(math)) # documentation of the module
#
# # ----------------------------------------
# # random module---------------------------
# to generate random numbers

from random import *
# # ---------------------------
# # 1. random() -- generate float value between 0 and 1
#
# for i in range(10):
#      print(random())

# # -----------------------------
# # 2. randint()  ---- generate random int value
#
# for i in range(10):
#      print(randint(1,10))

# # ---------------------------------
# # 3. uniform()---- to generate random float values between two numbers
#
# for i in range(10):
#     print(uniform(1,5))
#

# # ---------------------------------
# # 4. randrange(start,stop,step) ----
#
# print(randrange(11))
# print(randrange(1,11))
# print(randrange(1,11,2))
#
# for i in range(10):
#     print(randrange(1,11))


# # --------------------------------------
# # 5. choice() --  for choosing the value , it gives a random object from a given collection
#
# list1=['jay','siva','ashish','bhanu']
# for i in range(10):
#     print(choice(list1))
# ----------------
# list1=('jay','siva','ashish','bhanu')
# for i in range(10):
#     print(choice(list1))

# ## --------------
# #list1= {'jay', 'siva', 'ashish', 'bhanu'}  # set is not applicable
# #for i in range(10):
# #    print(choice(list1))



# # ------------------------------------------------------------
# # wap to generate a 6 digit random number as otp
#
# for i in range(10):
#     print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))

# for i in range(10):
#     # print(randint(000000,999999))  # it  may give a less number
#     print(randint(100000, 999999)) # it gives correct answer, but not give 0 at first place



# # ---------------------------------------------------------------
# # to generate random password of 6 length ------
# # 1,3,5 -- are alphabet symbols
# # 2,4,6 -- are digits
# #  example-- A4B6C8
#
# alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(10):
#     print(choice(alphabets),randint(0,9),choice(alphabets),randint(0,9),choice(alphabets),randint(0,9))
# print()
# print(choice(alphabets),randint(0,9),choice(alphabets),randint(0,9),choice(alphabets),randint(0,9))
# print()
#
#
# print(chr(randint(65,65+25)))
# print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9))
# print()
# for i in range(10):
#     print(chr(randint(65, 65 + 25)), randint(0, 9), chr(randint(65, 65 + 25)), randint(0, 9), chr(randint(65, 65 + 25)),randint(0, 9))






