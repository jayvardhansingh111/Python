
# =========================================================================================================

# Garbage collection :--- (Memory Management) waste useless object called garbage

# to destroy useless object called garbage collector


# gc module -------------------------------

# 1. gc.isenabled() --to check ga
# 2. gc.disable() -- to disable gc
# 3. gc.enable() -- to enable gc

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())






# =========================================================================================================

# Destructors : -- to perform clean up activities before destroying an object by the gc

# gc calls destructor automatically just before destroying an object
# to perform cleanup activities


# def __del__(self):    ---  syntax

import time

class Test:
    def __init__(self):
        print('object initialization')

    def __del__(self):
        print('fulfilling last wish and perform last wish')

# t=Test()
# print('Using t1 based on your requirement')
# time.sleep(5)
# print('work with t1 completed making eligible for gc')
# t=None
#
# time.sleep(10)
# print('end of application')



t1=Test()
t2=t1
t3=t2

del t1
time.sleep(5)
print('object yet not deleted after deleting t1')
del t2
time.sleep(5)
print('object yet not deleted after deleting t2')
del t3
time.sleep(5)
print('By this time object will be deleted')

print('end of application')





# -----------------------------

import time

class Test:
    def __init__(self):     # constructor
        print('object initialization')

    def __del__(self):      # destructor
        print('fulfilling last wish and perform last wish')

t=Test()
t1=None
print(t1)


list=[Test(),Test(),Test()]
del list
time.sleep(5)
print('End of application')



list=[Test(),Test(),Test()]
print('End of application')





# -----------------------------

import  sys
class Test:
    pass

t1=Test()
t2=t1
t3=t2
t4=t3
print(sys.getrefcount(t1))
del t2
print(sys.getrefcount(t1))
del t4,t3
print(sys.getrefcount(t1))

t1=None
print(sys.getrefcount(t1))





