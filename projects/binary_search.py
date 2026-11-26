# binary search --- it uses divide and  conquer , to search ordered list
import random
import time


# naive search
def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1




# binary search

def binary_search(l,target, low=None, high=None):
    if low is None:
        low =0
    if high is None:
        high = len(l) -1
    if high < low:
        return -1

    midpoint =(low+high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint-1)
    else:
        # target > l[midpoint]
          return binary_search(l,target,midpoint+1 , high)

if __name__ == '__main__':
    l=[1,2,3,4,10,15]
    target=7
    print(naive_search(l, target))
    print(binary_search(l, target))



    length = 10000
    # build sorted list
    sorted_lst= set()
    while len(sorted_lst) < length:
        sorted_lst.add(random.randint(-3*length, 3*length))
    sorted_lst = sorted(list(sorted_lst))

    start= time.time()
    for target in sorted_lst:
        naive_search(sorted_lst,target)
    end =time.time()
    print("Naive search time: ",(end-start)/length)

    start = time.time()
    for target in sorted_lst:
        binary_search(sorted_lst, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length)




