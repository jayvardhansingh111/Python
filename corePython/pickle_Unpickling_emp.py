import pickle, pickle_emp

f=open("emp.dat","rb")
print("Employee details....")

# print(pickle.load(f))
# print(pickle.load(f))
# print(pickle.load(f))  #EOFError: Ran out of input
# t=pickle.load(f)
# print(t)



while True:
    try:
        obj=pickle.load(f)
        obj.display()
        print()
    except EOFError:
        print("All employee details completed..")
        break
f.close()


f=open("emp.dat","rb")
print("Employee details....")
while True:
    try:
        obj=pickle.load(f)
        if obj. eno==100:
           obj.display()
           break
        print()
    except EOFError:
        print("All employee details completed..")
        break

f.close()
