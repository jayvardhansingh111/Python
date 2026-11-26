import pickle, pickle_emp

# with open("emp.dat",'wb') as f:
#     e=pickle_emp.Employee(100,'jay',10000,'gwl')
#     pickle.dump(e,f)
#     print("pickling method is completed...")


f=open("emp.dat","wb")
n=int(input("Enter the number of employees:"))
for i in range(n):
    eno=int(input("Enter the employee number:"))
    ename=input("enter the employee name:")
    esal=float(input("Enter the emp salary:"))
    eadd=input("Enter the emp address:")
    e=pickle_emp.Employee(eno,ename, esal, eadd)
    pickle.dump(e,f)


f.close()


