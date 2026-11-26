# Flow control ===> in which order the statement will execute is decided by flow control ======================================
#  3 types ----

# 1. Conditional statements / selection statements --------
# if, if-else, if-elif-else

# if (condition):
      # action

name=input("Enter name:")
if name=="jay":
    print("Hello jay")
    print("Hello jay")
    print("Hello jay")
print("how are you")


# if(condition):
#     # statement
# else:
#     # statement


if name=='jay':
    print("hello jay")
else:
    print("hello guest")
print("how are you")


# if(condition):
#     # statement
# elif:
#     # statement
# elif:
      # statement

brand=input("Enter brand name:")
if brand=="RC":
    print(" It is a children brand")
elif brand=="KF":
    print("it is for boys")
elif brand=="KO":
    print("it is for mens")
elif brand=="Kc":
    print("it is for legend")
else:
    print("it is not a brand")


 #wap to find biggest of 2 numbers from the keyword
n1=eval(input("Enter first number:"))
n2=eval(input("Enter second number:"))
if n1>n2:
    print("bigger number is :",n1)
else:
    print("bigger number is :",n2)



#  wap to find biggest of 3 numbers
n1=eval(input("Enter first number:"))
n2=eval(input("Enter second number:"))
n3=eval(input("Enter third number:"))
if n1>n2 and n1>n3:
    print("bigger number is :",n1)
elif n2>n3:
    print("bigger number is :",n2)
else:
    print("bigger number is :",n3)


#  wap to find number is evan or odd
n=eval(input("Enter the number:"))
if n%2==0:
    print(f"Number {n} is even")
else:
    print(f"Number {n} is odd")



# wap to check weather the given number is between 1 to 100
n=eval(input("Enter the number:"))
if n>=1 and n<=100:
    print(f"Number {n} is between 1 to 100")
else:
    print(f"Number {n} is not between 1 to 100")


# enter some digit from the keyword
# 0== ZERO
# 1== ONE
n=eval(input("Enter the number:"))
if n==0:
    print("number is ZERO")
elif n==1:
    print("number is One")
elif n==2:
    print("number is Two")
elif n==3:
    print("number is Three")
elif n==4:
    print("number is four")
elif n==5:
    print("number is five")
elif n==6:
    print("number is six")
elif n==7:
    print("number is seven")
elif n==8:
    print("number is eight")
elif n==9:
    print("number is nine")
else:
    print("Enter number between 0 to 9")


# wap to check
# 1=== one
# 12 == twelve
# 123 == one hundred and twenty three









# 2. Iterative statements -----------------------------------------------------------
# loops
# for loop, while
#---------------------------------------------------------
# for loop ----->know the number of iteration , used to iterate over a sequence -------------------------------------
# for eachElement in sequence:
   # statement

for i in range(1,10):
    print("i:",i)

s="jay vardhan singh"
count=0
for i in s:
    count += 1
    print(i)
print("the number of count:",count)

s=input("enter name:")
count=0
for i in s:
    count += 1
    print(i)
print("the number of count:",count)

s=input("enter name:")
count=0
for i in s:
    if count!= 0:
      print(f"the character {i} is present at {count} index")
    count += 1
print("the number of count:",count)


print("hello \n"*3)    # 0ne method to print
for i in range(1,11):   # second method to print
    print("hii",i)



# wap to print 0 to 20 only odd numbers
for i in range(21):   # first method
    if i%2!=0:
        print(i)
for i in range(21):    # second method
    if i%2==1:
        print(i)
for i in range(1,21,2):  # third method
    print(i)


#  wap to print 10 to 1 in descending order
for i in range(10,0,-1):
    print(i)
for i in range(10):
    print(10-i)

#  summation of list elements
list=eval(input("Enter the list:"))
sum=0
for x in list:
    sum+=x
    print("the sum is :",sum)
print("total sum is:",sum)




#  table of any number------------------
n=eval(input("enter digit:"))
for i in range(1,11):
    print(i*n)





# -----------------------------------------------------------------
# while loop ==> dont know the iteration time how many time executed
#  it worked till the condition is true
# while condition:
    # statement
x=1
while x<=10:
    print(x)
    x+=1



#  sum of first numbers ---------------
n=eval(input("enter number:"))
sum=0
i=1
while i<=n:
    sum= sum+i
    i= i+1
print("sum is :",sum)



#  some name from keyword ------------------------
# if the name is jay then continue otherwise ask again
name=""
while name != "jay":
    name=input("enter name:")
print("hello jay thanks for confirmation")


#  some name and password from keyword ------------------
# if the name is jay and password is 123 then continue otherwise ask again

name=""
password=""
while (name != "jay") or (password != "123"):
    name=input("enter name:")
    password=input("enter password:")
    if name !="jay" or password != "123":
        print("you entered wrong credentials.")
print("hello jay thanks for confirmation")



#  infinite loop ---> the loop is continuing forever  ====================================================
## while True:
##     print("hi jay")


i=0
while 1:
    print("hii")
    i+=1
    if i==5:
        break




# Nested loop ---> a loop inside a loop ---------------------------------------------------------------------
for i in range(1,4):
    for j in range(1,4):
        print("i={} and j is {}".format(i,j))



#  * pattern (90 degree triangle)-----------n number of row ---------------------
n=int(input("enter number of rows:"))
for i in range (1,n+1):   # i represents row number
    for j in range(i): # j represents column number
        print("*",end="")
    print()

n=int(input("enter number:"))
for i in range(1,n+1):
    print("*"*i)


# * pattern for square =----------------------------------------------------
n = int(input("enter number of rows:"))

for i in range(n):       # one method
    for j in range(n):
        print("*",end="")
    print()

for i in range(n):         # second method
    print(" * "*n)



# dimond pattern---------------------------------------------------------------
n = int(input("Enter number of rows: "))
# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))
# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))





# ------------------------------------------------------------------------
# 3. Transfer statements --------------------------------------------------------------------------------
# break , continue, pass

# -----------------------------------------------------
# 1. break ----> break th loop based on some condition ---------------------
for i in range(10):
    if i==8:
        print("processing is enough ....plz break ")
        break
    print(i)

card=[10,20,30,400,500,600,700,90,80]
for i in card:
    if i>500:
        print("you can by product from this card")
        break
    else:
        print("you cant buy that product ")



# -----------------------------------------------------------------------------------
# 2. continue --> skip current iteration and go for next iteration ---------------------------------------------------------------

for i in range(10):
    if i%2==0:
        continue
    print(i)

card=[10,20,30,400,550,600,700,90,80]
for i in card:
    if i>500:
        print("you can by product from this card")
        continue
    else:
        print("you cant buy that product ")



numbers=[10,0,20,30,0,400,550,600,700,90,80]
for i in numbers:
    if i==0:
        print("how can you divide zero by 100 ....")
        continue
    # print("100/{}={}".format(i,100/i))
    print("{}/100={}".format(i,i/100))





# ------------------------------------------------------------------------------
# 3. pass -----> don`t want to anything but do something ----------------------------------------------
# it is an empty statement , it won1t do anything
# don`t know the implementation in parent class then we use pass and define parent class in child class

# if True:
#     pass
# else:
    # print("hii")


def f1():
    print("hello")
def f2():
    pass
f1()
f2()

for i in range(50):
    if i%2==0:
        pass
    else:
        print(i)





#  del statement --> delete that variable if no longer required -------------------------------
#  use for memory management / utilization
x=10
print(x)
del x
# print(x) # error -> x is not define

s="jay"
a='ja'
print(s)
# del s[1] # cant delete character of string
del s ,a





# None ---> have no value , but variable is available  --------------------------
x=10
y=20
del x
# print(x) ## error
y= None
print(y) # give the value None



s1="jay"
s2="jay"
s3="jay"
print(id(s1), id(s2), id(s3))
del s1
print(s2, s3)

