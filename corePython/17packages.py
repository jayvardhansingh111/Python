# # packages concept -------------
# # to group related modules in a single packets is called as packages
# # it is a encapsulation mechanism to group related module into a single unit
#
# #  __init__.py  if this file is available inside the folder then it is considered as packages it is only in python 2 , not in python 3
#
#
#
# # --------------------------------------------------------------------------------
# # structure 1---------
#
# # | python_durgasir
# #       | 17packages.py
# #       | packages17pack1
# #                | module1.py
# #                | __init__.py
#
#
# import packages17pack1.module1
# packages17pack1.module1.f1()
#
#
# from packages17pack1.module1 import f1
# f1()
#
#
#
# # structure 2---------
#
# # | python_durgasir
# #       | 17packages.py
# #       | packages17pack1
# #                | module1.py
# #                | __init__.py
# #                | jaysoft
# #                     | module2.py
# #                     | __init__.py
#

#
from packages17pack1.module1 import f1
from packages17pack1.jaysoft.module2 import f2

f1()
f2()






# =====================================================================================================================

# Library --- contains several packages

# =======================================================================================


