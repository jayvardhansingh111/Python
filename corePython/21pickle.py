# pickling and unpickling of objects
# pickling -- the process of writing the total states of a file,i want to write total object to a file
# unpickling --  the process of reading the total states of a file, i want to read total object to a file

# pickle -- module

# dump(object,file)  -- to write
# load(file)         -- to read


# ------------------------------------------------
# class - Model / blueprint
# object - isinstance of class
# reference variable - variable name which refers to a object


# class Employee:
#     def __init__(self,eno,eName,eSal,eAdd):
#         self.eno=eno
#         self.eName=eName
#         self.eSal=eSal
#         self.eAdd=eAdd
#
# e=Employee(100,'jay',10000,'gwl')
# print(e.eno,e.eName,e.eSal,e.eAdd)





# ------------------------------------------------
import pickle

# class Employee:
#     def __init__(self,eno,ename,esal,eadd):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#         self.eadd=eadd
#     def display(self):
#         print(e.eno,'\t',e.ename,'\t',e.esal,'\t',e.eadd)

# with open("emp.dat",'wb') as f:
#     e=Employee(100,'jay',10000,'gwl')
#     pickle.dump(e,f)
#     print("pickling method is completed...")
#
#
# with open("emp.dat",'rb') as f:
#     obj=pickle.load(f)
#     print("print employee details after unpickling ....")
#     obj.display()
#     print(obj)



# ------------------------------------------------------------------------------








