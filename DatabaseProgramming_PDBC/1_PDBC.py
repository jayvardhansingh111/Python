# Python Database Programming ( PDBC) ---


# it is very common requirement to store data for future requirements

# ------------------------------------------------------------------------------
# 1. temporary storage ---

#  PVM memory areas


# ---------------------------------------------------------------------------------------
# 2. Permanent storage ---

#     1. File system
#     2. Database
#  etc.



# -----------------------------------------------
# 1. File system --- store very less amount of data

# Limitation:
# 1. Huge Data
# 2. No QL support
# 3. Security issue
# 4. Data inconsistency problem


# -----------------------------------------------
# 2. Database --- store huge amount of data, QL support
#              , Security is more, solve data inconsistency problem


# Limitations:
# 1. can not hold very huge amount of data like in TB
# 2. Structured data but not for unstructured data , semi structured







# =============================================================================================================

# Python Database Programming ( PDBC) ---

# cx_Oracle   --- for communicating to oracle database
# pymssql    --  for ms sql server
# pymysql   --    for mysql




# ------------------------------------------------------------
# Standard steps to communicate with database

# 1. import that database specific module

      # cx_Oracle   --- for communicating to oracle database
      # pymssql    --  for ms sql server
      # pymysql   --    for mysql

# 2. establish connection between python and db

      # con = cx_Oracle.connect(database information)

      # eg:
      # con = cx_Oracle.connect('Username/Password'@localhost)


# 3. Cursor object

      # cursor = con.cursor()

# 4. Execute our sql query

      # cursor.execute(sqlquery)  -- >  single query
      # cursor.executescript(sqlqueries)  -- >  to execute a group of queries string of sql queries separated by semicolon(;)
      # cursor.executemany()  --> to execute a parametrized query



# 5. Fetch the result

     # cursor.fetchone() --> fetch only one row
     # cursor.fetchall() --> fetch all rows
     # cursor.fetchmany(n) --> fetch n rows



# 6. commit()

     # con.commit() --> commit the transaction
     # con.rollback() --> rollback the transaction


# 7. close

     # cursor.close()
     # con.close()


