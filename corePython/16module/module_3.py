# # Reloading a module --------------------

# # -------------------------------------
# import module_1
# print("this is module 3...")
# # ---------------------------------------
#
# import time
# from  importlib import reload
# import module_1
#
# print("program entering in sleeping state")
# time.sleep(20)
#
# reload(module_1)
# print("program entering into sleeping state....")
# time.sleep(20)
# reload(module_1)
# print("this is last line of program..")



# -------------------------------------------------
# finding members of module using dir

# dir()-- for finding the members of module ----
# import time
# import importlib
# import module_1
# print(dir(time))
# print(dir(importlib))

# print(dir(module_1))

# print(__builtins__)  #<module 'builtins' (built-in)>
# print(__doc__) # None
# print(__cached__)   # None
# print(__file__)      # path of the file
# print(__loader__)      # loader object
# print(__name__)  # __main__
# print(__package__)  # None
# print(__spec__)  # None
# print(__name__)  #__main__



# ------------------------------------------------------------------
# the special variable   __name__     -----------------

import module_1
print("from module_3... we are executing module_1 ( f1() )..")
module_1.f1()




















