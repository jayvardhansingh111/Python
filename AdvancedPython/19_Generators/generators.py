# Generator --
#             generator is function which is responsible for generate a sequence of values.
#             it did not store all the values in the memory . it generates the values at the time of need.
#   it uses yield keyword to return the values



# ---------------------------------------------
l= [x*x for x in range(10)]
print(l[1])

# l= [x*x for x in range(10000000000000)]  # memoryError --> too much value
# print(l[1])
#
# ---------------------------------------------
#
#
# --------------------------------------------------------------------------------------
# generators -----------------

g= (x*x for x in range(10))
print(next(g))
print(next(g))
print(next(g))

g= (x*x for x in range(10000000000000)) # memoryError --> too much value
print(next(g))
print(next(g))
print(next(g))





def my_generator():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'

g=my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # error , no next values




# ques -- generate first n numbers

def first_n(num):
    n=1
    while n<=num:
        yield n
        n=n+1

# values=first_n(1000000000)
values=first_n(5)
for x in values:
    print(x)





def countdown(num):
    print("Countdown started")
    while num>0:
        yield num
        num=num-1

values=countdown(5)
for x in values:
    print(x)





# generate fibonacci numbers

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fibonacci():
    if f < 1000:
       print(f)
    else:
        break



from random import *
import time

def name_generators():
    alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # name=''
    while True:
        name = ''
        for i in range(6):
            name += choice(alphabets)
        yield name

for i in name_generators():
    time.sleep(2)
    print(i)




from random import *
import time

names=['sunny','bunny','chinny','vinny']
subjects=['python','java','c++']

def people_list(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'name':choice(names),
            'subject':choice(subjects)
        }
        results.append(person)
    return results


def people_generator(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'name':choice(names),
            'subject':choice(subjects)
        }
        yield person


t1=time.time()
people_list(100000)
t2=time.time()
print('Time taken:',t2-t1)


t1=time.time()
people_generator(100000)
t2=time.time()
print('Time taken:',t2-t1)











