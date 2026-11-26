# --------------------------------------------------------------------------------------
# levels of logging:
# 1.  CRITICAL --> 50    ---> represents very serious problem that need to high attention
# 2.  ERROR --> 40       ---> represents a serious error
# 3.  WARNING --> 30    ---> alert the programmer
# 4.  INFO--> 20
# 5.  DEBUG--> 10
# 6.  NOTSET--> 0


import  logging
logging.basicConfig(filename='student.txt',level=logging.INFO)
logging.info('info message from student module')

# either  info or higher message written
