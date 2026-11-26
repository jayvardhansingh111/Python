# Logging :-- to store complete application flow and exception information to a file
#             by using log file we can debug
#
#
# --------------------------------------------------------------------------------------
# levels of logging:
# 1.  CRITICAL --> 50    ---> represents very serious problem that need to high attention
# 2.  ERROR --> 40       ---> represents a serious error
# 3.  WARNING --> 30    ---> alert the programmer
# 4.  INFO--> 20
# 5.  DEBUG--> 10
# 6.  NOTSET--> 0




# ----------------------------------------------------------------------------------
# how to implement logging:
#
# where logging data
# data
#
# import logging
# logging.basicConfig(filename='log.txt',level=30)
# logging.debug(massage)
# logging.info(massage)
# logging.warning(massage)
# logging.error(massage)
# logging.critical(massage)
# logging.NOTSET(massage)




# WAP to create a log file and write warning and higher level messages ?

import logging

logging.basicConfig(filename='log.txt',level=logging.WARNING)
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo")



logging.basicConfig(filename='log.txt')  # default level warning
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo1")




logging.basicConfig(filename='log.txt',level=10)  # level 10 for all the data
# logging.basicConfig(filename='log.txt',level=logging.WARNING)
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo2")



# -----------------------------------------------------------------------------------------------------
# default filename is console -- data is written in console if file is not given

logging.basicConfig()
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo2")





logging.basicConfig()
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo2")




# -----------------------------------------------------------------------------------
# for override data in the log file we use the "filemode" --> 'w'

logging.basicConfig(filename='log.txt',filemode='w',level=40)
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo with the override .....")



# default level =WARNING(30)
# default FILE = console
# default mode = append


# ------------------------------------------------------
# How to format log messages :
#         format keyword argument we can format message

# 1. To display only level
# logging.basicConfig(format='%(levelname)s')


logging.basicConfig(format='%(levelname)s')
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo  .....")




# 2. To display  level and message
# logging.basicConfig(format='%(levelname)s:%(message)s')


logging.basicConfig(format='%(levelname)s :%(message)s')
logging.debug('Debug massage')
logging.info('Info massage')
logging.warning('Warning massage')
logging.error('Error massage')
logging.critical('Critical massage')

print("Logging demo  .....")





# 3. To display  timestamp in the log message
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')


logging.basicConfig(filename='log.txt',filemode='w',format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

print("Logging demo  .....")




# --------------------------------------------------------------------------------------------------
# how to change date and time format
#   datefmt='%d/%m/%Y' ---> 12/07/2026
#   datefmt='%d/%m/%Y  %I:%M:%S %p'  ---> 12/07/2026  hours:minutes:second am/pm   --> 12 hours
#   datefmt='%d/%m/%Y  %H:%M:%S %p'  ---> 12/07/2026  hours:minutes:second    --> 24 hours


logging.basicConfig(filename='log.txt',filemode='w',format='%(asctime)s:%(levelname)s:%(message)s'
                    ,datefmt='%d/%m/%Y')
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

print("Logging demo  .....")



logging.basicConfig(filename='log.txt',filemode='w',format='%(asctime)s:%(levelname)s:%(message)s'
                    ,datefmt='%d/%m/%Y  %I:%M:%S %p',level=10)
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

print("Logging demo  .....")



logging.basicConfig(filename='log.txt',filemode='w',format='%(asctime)s:%(levelname)s:%(message)s'
                    ,datefmt='%d/%m/%Y  %H:%M:%S %p',level=10)
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

print("Logging demo  .....")





# How to write exceptions to the log file:
# logging.exception(message)

logging.basicConfig(filename='log.txt',datefmt='%d/%m/%Y  %I:%M:%S %p',level=10)
logging.info('A new request came.')
try:
    x=int(input('Enter first number: '))
    y=int(input('Enter second number: '))
    print('Division is: ',x/y)
except ZeroDivisionError as msg:
    print('Can not divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('Please provide int value only')
    logging.exception(msg)

logging.info('Request processing completed')

