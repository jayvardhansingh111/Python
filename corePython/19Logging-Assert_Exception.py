# Logging :-- to store complete application flow and exception information to a file
# by using log file we can debug


# ----------------------------------------
# levels of logging:
# 1. CRITICAL --> 50
# 2. ERROR --> 40
# 3. WARNING --> 30
# 4. INFO--> 20
# 5. DEBUG--> 10
# 6. NOTSET--> 0


# ----------------------------------------
# HOW TO IMPLEMENT LOGGING--
# basicConfig() of logging module
# logging.basicConfig(filename='log.txt',level=logging.WARNING)

# logging.debug(massage)
# logging.info(massage)
# logging.warning(massage)
# logging.error(massage)
# logging.critical(massage)


# ----------------------------------------
# wap to create a log file and write WARNING and Higher Level Massage
import logging


logging.basicConfig(filename='log.txt',level=logging.WARNING)
print("python logging demo")
logging.debug("debug massage")
logging.info("info massage")
logging.warning("warning massage")
logging.error("error massage")
logging.critical("critical massage")

print()
logging.basicConfig(filename='log.txt')
print("python logging demo")
logging.debug("debug massage")
logging.info("info massage")
logging.warning("warning massage by default")
logging.error("error massage")
logging.critical("critical massage")

print()

logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print("python logging demo")
logging.debug("debug massage by debug")
logging.info("info massage")
logging.warning("warning massage ")
logging.error("error massage")
logging.critical("critical massage")


# ----------------------------------------
# wap to write exceptions information to the log file

logging.basicConfig(filename='log.txt',level=logging.INFO)
logging.info("A new request came")
try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    print("The result is:",x/y)
except ZeroDivisionError as msg:
    print("can not divide with zero.")
    logging.exception(msg)
except ValueError as msg:
    print("please provide the int value only.")
    logging.exception(msg)
logging.info("Request processing completed")



logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%d/%m/%y %I:%M:%S %p'
)
logging.info("A new request came")

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("The result is:", x / y)

except ZeroDivisionError as msg:
    print("can not divide with zero.")
    logging.exception(msg)

except ValueError as msg:
    print("please provide the int value only.")
    logging.exception(msg)
logging.info("Request processing completed")



# ================================================================================================================

#  debugging -- the process of finding and fix the bug
#
# -------------------------------------------------------------------------------
#
# assert -- for debugging , to alert the programmer to resolve development time error
#
# 1. simple version
# 2. very simple version(augmented version)
#
# assert conditional_expression
#
# assert conditional_expression, message


# -----------------------
# 1. simple version
x=10
assert x==10
# assert x>10




print(x)



# -----------------------
# 2. very simple version(augmented version)

x=10
assert x==10,'here x value should be 10 but not'




# assert x>10 ,'here x value should be >10 but not'




print(x)

# ----------------------------------------

# def square(x):
    # return x**x

# assert square(2)==4,'the square of 2 is 4 '
# assert square(3)==9,'the square of 3 is 9 '
#
#
# print(square(2))
# print(square(3))
# print(square(4))
# print(square(5))


def square(x):
    return x*x

assert square(2)==4,'the square of 2 is 4 '
assert square(3)==9,'the square of 3 is 9 '


print(square(2))
print(square(3))
print(square(4))
print(square(5))
