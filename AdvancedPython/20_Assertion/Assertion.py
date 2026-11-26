# Assertions -- Debugging Purpose
#            -- An assertion is a debugging statement used to check whether a condition is True.
#               If the condition is False, Python raises an AssertionError.
#
#         --- Assertions are mainly used during development to detect programming errors early.


# Debugging ------
#            7The process of identify and fix the bug


# assert -- for debugging , to alert the programmer to resolve development time error



# --------------------------------------------------------------
# types of assert statements ---

# 1. Simple version
# 2. More simple version / augmented

# assert conditional_expression  --> simple
# assert conditional_expression , massage --> augmented


# 1. Simple version -------

# syntax:
#           assert b

            # if b is true means our condition satisfied. up to this there
            #  is no problem and execution will be continued.

            # if b is false means somewhere something goes wrong. stop the
            # program execution by raising AssertionError


# 2. More simple version / augmented


# --------------------------------------------------------------

def square_it(n):
    return n*n

assert square_it(2)==4,'The square of 2 should be 4'
assert square_it(3)==9,'The square of 2 should be 9'
assert square_it(4)==16,'The square of 2 should be 16'
assert square_it(5)==25,'The square of 2 should be 24'


print(square_it(2))
print(square_it(3))
print(square_it(4))
print(square_it(5))
