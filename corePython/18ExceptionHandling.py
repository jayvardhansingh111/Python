# exception handling --
# a mechanism used to manage the runtime errors  known as exceptions
# and handle that errors without crash is known as exception handling


# types of errors ----
# -----------------------------------------------------------------
# 1. syntax Errors -- if we enter invalid syntax then the get syntax errors

# x=10
# if x==10     # : missing so it gives syntax errors
#     print("x value is:",x)
# print"hii"  # () are missing


# ---------------------------------------------------------------------------------
# 2. runtime Errors (exceptions)-- while executing the program if something goes wrong then we will get the runtime errors

# print(10/0)   #ZeroDivisionError: division by zero
# print(10/'ten')  #TypeError: unsupported operand type(s) for /: 'int' and 'str'


# x=int(input("Enter some number:"))
# print(x)


# ===========================================================================
# what is exception : ---
#  some unwanted unexpected event disturb normal flow of the program

# # example:
# ZeroDivisionError
# TypeError
# ValueError
# FileNotFoundError
# FileExistsError
# EOFError


# it is highly to handle expections
# Graceful termination of the program



# -----------------------------------------
# what is the meaning of exception handling ?
# - defining alternative way to continue rest of the program

# try:
#     read data from remote file
# except FileNotFoundError:
#     use local file and continue rest of the program
#


# --------------------------------------------

print("hello")
# print(10/0)     # Risky code -- we take it in the try block
print("hii")


# --------------------------------------------

# try:
#     Risky code
# except:
#     Handling code

print("hello")
try:
  print(10/0)     # Risky code -- we take it in the try block
except ZeroDivisionError:
    print("how can you divide something by zero")
    print(10/2)
print("hii")

print("hello")
try:
  print(10/0)     # Risky code -- we take it in the try block
except ArithmeticError:
    print("how can you divide something by zero")
    print(10/2)
print("hii")


print("hello")
try:
  print(10/0)     # Risky code -- we take it in the try block
except BaseException:  # it working but not recommended
    print("how can you divide something by zero")
    print(10/2)
print("hii")




# ====================================================================================================
# control flow of try-except block ------------------------
# ---------------------------------
# how to print exception information
try:
  print(10/0)
except ZeroDivisionError as msg:
    print("Exception raised and its massage is:",msg)



# -------------------------------------------------------------------
# try with multiple except block ------

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
# except ArithmeticError:
#     print("it is arithemetic error")
except ZeroDivisionError:
    print("can not divide with zero")
except ValueError:
    print("please provide int value only")




# ---------------------------------------------
# single except block can handle multiple exceptions
# except(exception1,exception2,.......) :
#     handling code

# except(exception1,exception2,.......) as msg :
#     handling code

try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
except (ZeroDivisionError,ValueError) as msg:
    print("please provide valid number and the problem is:",msg)



# ---------------------------------------------
# Default except block --------


try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print(x/y)
except ZeroDivisionError as msg:
    print("please provide valid number and the problem is:",msg)
except:   # default except must be last
    print("Default except block: plz provide valid value")


# ======================================================================
# finally block -- to maintain clean up code , weather the exceptions rise or not rise it get the chance every time

# case 1---
try:
    print("try")
except ZeroDivisionError:
    print("except")
finally:
    print("finally")


# case 2--
try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")


# case 3----
# try:                  # first executed
#     print("try")
#     print(10/0)
# except ValueError:      # third executed
#     print("except")
# finally:                 # second executed
#     print("finally")



# case 3----
import os
try:                  # first executed
    print("try")
    os._exit(0)
except ValueError:      # third executed
    print("except")
finally:                 # second executed
    print("finally")







# ======================================================================
# Nested try-except=finally -------

try:
    print("outer try block.")
    try:
        print("inner try block.")
        print(10/0)
    except ZeroDivisionError:
        print("inner except block.")
    finally:
        print("inner finally block.")
except :
    print("outer except block.")
    # try:
    # except:

finally:
    print("outer finally block")
    # try:
    # except:
#



# ----------------------------------------------------------------
# else block -- if no exceptions in try block then else block executed
#
# try:
#     Risky code
# except :
#     will be executed if exception in try
# else:
#     will be executed if no exception in try
# finally:
#     will be executed always

try:
    print("try.")
except :
    print("except.")
else:
    print("else.")
finally:
    print("finally")


print("new line.........")
try:
    print("try.")
    print(10/0)
except :
    print("except.")
else:
    print("else.")
finally:
    print("finally")








# --------------------------------------------------------------------
# Various possible combination of try-except-else-finally  block.

#---------------------------------------
# 1. try-expect   -- valid
try:
    print("try.")
except:
    print("except.")

#---------------------------------------
# 2. try-finally  --  valid
try:
    print("try.")
finally:
    print("finally.")
#---------------------------------------
# 3. try-except-else --valid
try:
    print("try.")
except:
    print("except.")
else:
    print("else.")

#---------------------------------------
# # 4.  try-else --invalid
# try:
#     print("try.")
# else:                 # invalid use except block then use else block
#     print("else.")


#---------------------------------------
# # 5. try-else-finally  -- invalid

# try:
#     print("try.")
# else:
#     print("else.")
# finally:
# print("finally.")
print("h")



#---------------------------------------
# 6. try-except-except-except-.... --valid
try:
    print("try.")
except ZeroDivisionError:
    print("except.")
except ValueError:
    print("except.")
except:
    print("except.")



#---------------------------------------
# 7. try-except-finally-finally -- invalid (we can use finally only one time in a except block)

# try:
#     print("try.")
# except ZeroDivisionError:
#     print("except.")
# finally:
#     print("finally")
# finally:
#     print("finally")


#---------------------------------------
# # 8. try-else-else-finally  -- invalid

# try:
#     print("try.")
# else:
#     print("else.")
# else:
#     print("else.")
# finally:
# print("finally.")
print("h")


#---------------------------------------
# 9. try-except-else-else  -- invalid

# try:
#     print("try.")
# except:
#     print("except")
# else:
#     print("else.")
# else:
#     print("else.")


# #---------------------------------------
# 10 try- print -except  --invalid

# try:
#     print("try")
# print("hello")
# except:
#     print("except")


# #---------------------------------------
# 11. try-except-except --invalid

# try:
#     print("try")
# except:
#     print("except")
# print("hello")
# except:
#     print("except")


#---------------------------------------
# 12. try-except-try-finally -- valid
try:
    print("try")
except:
    print("except")
try:
   print("try")
finally:
    print("finally")


#---------------------------------------
# 13  try-except-try-except -- valid

try:
    print("try")
except:
    print("except")
try:
   print("try")
except:
    print("finally")

#---------------------------------------
# 14. try-except-if-else --Valid
try:
    print("try")
except:
    print("except")
if 10>20:
   print("if")
else:
    print("else")

# #---------------------------------------
# 15.  try(try-except-finally)-except-finally -- valid
try:
    print("try")
    try:
        print("inner try")
    except:
        print("inner except")
    finally:
        print("inner finally")
except:
    print("except")
finally:
    print("finally")


#---------------------------------------
# 16.  try-except(try-except-finally)-finally -- valid
try:
    print("try")
except:
    print("except")
    try:
        print("inner except try block")
    except:
        print("inner except")
    finally:
        print("inner finally")
finally:
    print("finally")

# #---------------------------------------
# 17.  try-except-finally(try-except-finally)  --valid
try:
    print("try")
except:
    print("except")
finally:
    print("finally")
    try:
        print("inner finally try block")
    except:
        print("inner except")
    finally:
        print("inner finally")

#---------------------------------------
# 18 try(try)-except -- invalid

# try:
#     print("try")
#     try:
#         print("inner try")
# except:
#     print("except")


#------------------------------------------------------------------------------------------------------------------
# 1. try block compulsory we should write either except or finally
# 2. except without try is invalid
# 3. finally without try is invalid
# 4. we can take multiple except block for the same try but we can not take multiple try for the same except block
# 5. else without is invalid
# 6. try-except-else-finally -- order is important
# 7. we can take try-except-else-finally inside try,except,else,finally blocks  , -- Nesting of try-except-else-finally is valid
#------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------
# Types of exceptions ---
# 1. predefined exceptions / inbuilt exceptions
# 2. user defined exceptions / customized exceptions

# ---------------------------------------
# 1. predefined exceptions / inbuilt exceptions
#  the exceptions which are raised automatic by python whenever a particular event occurs

# eg1.  print(10/0) -- ZeroDivisionError

# eg2.  print(10/ff) -- ValueError

# ---------------------------------------
# 2. user defined exceptions / customized exceptions
# the exceptions which are raised by the programmer when the particular event occurs

# -------------------------
# every exception in python is a class

# class className(Parent):
#     def __init__(self,args):
#         self.msg=args

class TooYoungException(Exception):
    def __init__(self,args):
        self.msg=args

class TooOldException(Exception):
    def __init__(self,args):
        self.msg=args

age=int(input("Enter age:"))
if age<18:
    raise TooYoungException("to young for voiting")
elif age>=18:
    raise TooOldException("ready for voiting")
else:
    print("thanks for registration")




