# # --------------------------------------------------------------------------------------
# # levels of logging:
# # 1.  CRITICAL --> 50    ---> represents very serious problem that need to high attention
# # 2.  ERROR --> 40       ---> represents a serious error
# # 3.  WARNING --> 30    ---> alert the programmer
# # 4.  INFO--> 20
# # 5.  DEBUG--> 10
# # 6.  NOTSET--> 0
# # --------------------------------------------------------------------------------------

#
# import logging
# import student
#
# logging.basicConfig(filename='login99.txt',level=50)
# logging.warning('warning message from 2_login module')
# logging.critical('critical message from 2_login module')
# logging.info('info message from 2_login module')
# logging.error('error message from 2_login module')
# logging.debug('debug message from 2_login module')
#
#
# #  once the configuration is set in the parent or the same file then that configuration is only consider





# # ---------------------------------------------------------------------------------------------------------------------------------
# import logging
#
# # Advanced Logging : Customized Logger :
# # steps : ----
#
# # 1. creation of logger object and set log level.
# logger = logging.getLogger("demologger")
# logger.setLevel(logging.INFO)
#
#
# # 2. creation of handler object and set log level.
# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.INFO)
#
#
# # 3. creation of formatter object
# formatter = logging.Formatter(
#     fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %I:%M:%S %p"
# )
#
# # 4. Add Formatter to Handler
# consoleHandler.setFormatter(formatter)
#
#
# # 5. Add handler to object
# logger.addHandler(consoleHandler)
#
#
# # 6. Write messages by using logger object with the following method
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")






import logging

logger = logging.getLogger("demologger")
logger.setLevel(logging.INFO)


consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

fileHandler= logging.FileHandler('student.txt')
fileHandler.setLevel(logging.ERROR)


formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p"
)

formatter1 = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S %p"
)

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter1)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

