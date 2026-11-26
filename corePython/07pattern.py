# # Nested loop ---> a loop inside a loop ---------------------------------------------------------------------
# for i in range(1,4):
#     for j in range(1,4):
#         print("i={} and j is {}".format(i,j))



# #  * pattern (90 degree triangle)-----------n number of row ---------------------
# n=int(input("enter number of rows:"))
# for i in range (1,n+1):   # i represents row number
#     for j in range(i): # j represents column number
#         print("*",end="")
#     print()

# n=int(input("enter number:"))
# for i in range(1,n+1):
#     print("*"*i)


# # * pattern for square =----------------------------------------------------
# n = int(input("enter number of rows:"))
#
# for i in range(n):       # one method
#     for j in range(n):
#         print("*",end="")
#     print()
#
# for i in range(n):         # second method
#     print(" * "*n)



# # dimond pattern---------------------------------------------------------------
# n = int(input("Enter number of rows: "))
# # Upper part
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2*i - 1))
# # Lower part
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2*i - 1))
#







# # 1. Print a Square Pattern
# # *****
# # *****
# # *****
#
# n= int(input("Enter the number of rows:"))
# for i in range(n):   # using two loops
#     for j in range(n):
#         print("*",end="")
#     print()
# for i in range(n):  # using one loop
#     print("* "*n)

#
# # 2. Print a Right Triangle
# # *
# # **
# # ***
# # ****
# # *****
#
# n=int(input("Enter the row number:"))
# for i in range(1,n+1):
#     print("*"*i)
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("8",end='')
#     print()



# # 3. Print an Inverted Right Triangle
# # *****
# # ****
# # ***
# # **
# # *
# n=int(input(" enter number of row:"))
# for i in range(n-1,0,-1):
#     print("*"*i)
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()




# # 4. Print a Pyramid Pattern
# #     *
# #    ***
# #   *****
# #  *******
# # *********
#
# n = int(input(" enter number of rows:"))
#
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2*i - 1))
#
#
# for i in range(1, n + 1):
#     # printing spaces
#     for j in range(n - i):
#         print(" ", end="")
#     # printing stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()   # move to next line


#
# # 5. Print an Inverted Pyramid
# # *********
# #  *******
# #   *****
# #    ***
# #     *
#
# n=int(input("Enter the number of rows:"))
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(n,0,-1):
#     for j in range(n-i,0,-1):
#         print(" ",end='')
#     for k in range(2*i-1):
#         print("*",end='')
#     print()


#
# # 6. Print a Diamond Pattern
# #     *
# #    ***
# #   *****
# #  *******
# # *********
# #  *******
# #   *****
# #    ***
# #     *
# #
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))
#
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end='')
#     for k in range(2*i-1):
#         print("*",end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end='')
#     for k in range(2*i-1):
#         print("*",end='')
#     print()



# # 7. Print a Hollow Square
# # *****
# # *   *
# # *   *
# # *   *
# # *****
# #
# n = int(input("Enter the number of rows: "))
#
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#


# 8. Print a Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********
#

n = int(input(" enter number of rows:"))

for i in range(1, n + 1):
    for j in range(1,n+1):
      if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
      else:
            print(" ", end="")
print()

    # print(" " * (n - i) + "*" * (2*i - 1))







# for i in range(1, n + 1):
#     # printing spaces
#     for j in range(n - i):
#         print(" ", end="")
#     # printing stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()   # move to next line










# 9. Print a Hollow Diamond
#     *
#    * *
#   *   *
#  *     *
#   *   *
#    * *
#     *
#
# 🔢 Number Pattern Questions
# 10. Print Number Triangle
# 1
# 12
# 123
# 1234
# 12345
#
# 11. Print Repeated Number Triangle
# 1
# 22
# 333
# 4444
# 55555
#
# 12. Print Floyd’s Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
#
# 13. Print Pascal’s Triangle
#     1
#    1 1
#   1 2 1
#  1 3 3 1
#
# 14. Print Reverse Number Triangle
# 12345
# 1234
# 123
# 12
# 1
#
# 15. Print Pyramid of Numbers
#     1
#    121
#   12321
#  1234321
# 123454321
#
# 🔤 Alphabet Pattern Questions
# 16. Print Alphabet Triangle
# A
# AB
# ABC
# ABCD
# ABCDE
#
# 17. Print Repeated Alphabet Pattern
# A
# BB
# CCC
# DDDD
# EEEEE
#
# 18. Print Alphabet Pyramid
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
#
# 🔥 Advanced Pattern Questions (Very Important)
# 19. Print X Pattern
# *   *
#  * *
#   *
#  * *
# *   *
#
# 20. Print Plus (+) Pattern
#   *
#   *
# *****
#   *
#   *
#
# 21. Print Butterfly Pattern
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
#
# 22. Print Sandglass Pattern
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
#
# 23. Print Spiral Matrix Pattern (Most Asked)
#
# Example for 4x4:
#
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7
#
# 24. Print Checkerboard Pattern
# * * * *
#  * * * *
# * * * *
#  * * * *
#
# 25. Print 0-1 Triangle
# 1
# 01
# 101
# 0101
# 10101
#
# ✅ Exam Special Question Set (Most Common)
#
# ✔ Star Pyramid
# ✔ Diamond Pattern
# ✔ Hollow Square
# ✔ Hollow Diamond
# ✔ Floyd Triangle
# ✔ Pascal Triangle
# ✔ Number Palindrome Pyramid
# ✔ Butterfly Pattern
# ✔ X Pattern
# ✔ Spiral Matrix
#
# If you want, I can also provide solutions of all these patterns in Python one by one.
#
# also give the questions that may be asked in interview
#
# Sure. In interviews, pattern questions are asked to test your logic, loops, nested loops, and string handling. Here are the most common ones:
#
# ✅ Most Asked Pattern Questions in Python Interviews
# ⭐ Star Pattern Interview Questions
# 1. Print Right Triangle
# *
# **
# ***
# ****
# *****
#
# 2. Print Inverted Triangle
# *****
# ****
# ***
# **
# *
#
# 3. Print Pyramid (Centered Triangle)
#     *
#    ***
#   *****
#  *******
# *********
#
# 4. Print Inverted Pyramid
# *********
#  *******
#   *****
#    ***
#     *
#
# 5. Print Diamond Pattern
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
#
# 6. Print Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
#
# 7. Print Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********
#
# 8. Print Hollow Diamond
#     *
#    * *
#   *   *
#  *     *
#   *   *
#    * *
#     *
#
# 9. Print Butterfly Pattern
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
#
# 10. Print Sandglass Pattern
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
#
# 🔢 Number Pattern Interview Questions
# 11. Print Number Triangle
# 1
# 12
# 123
# 1234
# 12345
#
# 12. Print Repeated Number Triangle
# 1
# 22
# 333
# 4444
# 55555
#
# 13. Print Reverse Number Triangle
# 12345
# 1234
# 123
# 12
# 1
#
# 14. Print Floyd’s Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
#
# 15. Print Pascal Triangle
#     1
#    1 1
#   1 2 1
#  1 3 3 1
#
# 16. Print Number Pyramid Palindrome
#     1
#    121
#   12321
#  1234321
# 123454321
#
# 17. Print 0-1 Triangle
# 1
# 01
# 101
# 0101
# 10101
#
# 🔤 Alphabet Pattern Interview Questions
# 18. Print Alphabet Triangle
# A
# AB
# ABC
# ABCD
# ABCDE
#
# 19. Print Repeated Alphabet Triangle
# A
# BB
# CCC
# DDDD
# EEEEE
#
# 20. Print Alphabet Pyramid
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
#
# 🔥 Advanced Interview Pattern Questions
# 21. Print X Pattern
# *   *
#  * *
#   *
#  * *
# *   *
#
# 22. Print Cross (+) Pattern
#   *
#   *
# *****
#   *
#   *
#
# 23. Print Zig-Zag Pattern
#
# Example:
#
# *   *   *
#  * * * *
#   *   *
#
# 24. Print Spiral Matrix (Very Important)
#
# Example for 4x4:
#
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7
#
# 25. Print Pyramid using numbers in continuous sequence
# 1
# 2 3
# 4 5 6
# 7 8 9 10
#
# ✅ Common Interview Twisted Pattern Questions
# 26. Print pattern without using nested loops
#
# (Using string multiplication or recursion)
#
# 27. Print diamond using a single loop
# 28. Print pattern using recursion
# 29. Print hollow patterns using condition checks
# 30. Print pattern for any input size n (dynamic pattern)
# 💡 Most Common Interview Question Statements
#
# Interviewers may ask like this:
#
#  "Write a program to print a pyramid pattern for n rows."
#  "Print a hollow diamond pattern using loops."
#  "Print Floyd’s triangle using nested loops."
#  "Print a butterfly pattern."
#  "Print spiral matrix in clockwise direction."




