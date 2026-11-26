# File handling --- to store data permanently in a file for the future purpose
# File Handling in Python means creating, reading, writing, and managing files stored on the computer
#
# open()
# read()
# write()
# close()
#
#
#  Steps of File Handling ----------------
#
# 1. Open the file
# 2. Perform operations (read/write)
# 3. Close the file
#
#
#
# types of files ------------
# 1. Text file  -- to store character data
# 2. Binary file -- to store binary data like image, video, audio.
#
#
# --------------------------------------
# opening a file ---  open()
# f=open(filename,mode)
#
# --------------------------------------------------------------------------------------------
# modes --------------
#
# 1. Text file----------
#
# 1. r -- for read operation , it is default modde
# 2. w -- for write operation , it will overwrite the data written in the file
# 3. a -- for append operation, not override , create the file if not exist
# 4. r+ -- read and write operation , not override data, not deleted data
# 5. w+ -- write and read operation , override the existing data
# 6. a+ -- append and read data, not override existing data
# 7. x -- create the file if not exist , if exist then raise the FileExistError .
#
#
# 2. Binary file ---------------
# rb, wb, ab, r+b, w+b, a+b ,
#
#
# after completing the operation we need to close the file
# f.close()
#
#
#
# --------------------------------------------------------------------
# various properties of file object --
#
#           these are variables
# f.name
# f.mode
# f.closed
#
#           methods
# f.readable()
# f.writable()

# ==========================================================================================================
# 1. Text file Reading -- to store character data


f=open("abcFileHandling.txt",'w')
print("file name:",f.name)
print("file mode:",f.mode)
print("is file readable:",f.readable())
print("is file writeable:",f.writable())

print("is file closed:",f.closed)
f.close()
print("is file closed:",f.closed)



# f=open("xyFileHandling.txt",'r')    # FileNotFoundError, file is not available
# print("file name:",f.name)
# print("file mode:",f.mode)
# print("is file readable:",f.readable())
# print("is file writeable:",f.writable())
#
# print("is file closed:",f.closed)
# f.close()
# print("is file closed:",f.closed)

print()
# this code can run only one time because 'x' mode

# f=open("xyFileHandling.txt",'x')
# print("file name:",f.name)
# print("file mode:",f.mode)
# print("is file readable:",f.readable())
# print("is file writeable:",f.writable())
#
# print("is file closed:",f.closed)
# f.close()
# print("is file closed:",f.closed)




# ---------------------------------------------------
# writing data to the text file :-

# f.write(str)
# f.writelines(list of lines)

f=open("abcFileHandling.txt",'w') # it override the data
print("file name:",f.name)
print("file mode:",f.mode)
f.write('jay\n')
f.write('vardhan\n')
f.write('singh\n')
f.write('hello\n')
f.close()


f=open("abcFileHandling.txt",'a') # it appended the data not override
print("file name:",f.name)
print("file mode:",f.mode)
f.write('jay\n')
f.write('vardhan\n')
f.write('singh\n')
f.write('hello, data written successfully\n')
f.close()



f=open("abcFileHandling.txt",'w')
print("file name:",f.name)
print("file mode:",f.mode)
list1=['jay\n','ashish\n','siva\n','bhanu\n']
f.writelines(list1)
print("Data written successfully.....")
f.close()

#
# -------------------------------------------------------
#  reading character data from the file
#
# read() -- to read total data from the file
# read(n) -- to read 'n' character from the file
# readline() -- to read only one line
# readlines() -- to read all lines into a list


f=open('abcFileHandling.txt','r')

# data=f.read()
# print(data)
#
# data1=f.read(10)
# print(data1)
#
# data=f.readline()
# print(data)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
#
#
list=f.readlines()
print(list)
for i in list:
    print(i)

f.close()

# -----------------------------------------------
# The with statement --
# it will tale care closing of file while, after completing all the operations
# it used while opening a file

with open('abcFileHandling.txt','w') as f:
    f.write("JAY\n")
    f.write("var\n")
    f.write("dhan\n")
    f.write("SINGH\n")
    print("is file closed ?:",f.closed)

print("is file closed ?:",f.closed)



# ---------------------------------------------------
# tell() -- it return the current position of pointer(cursor)

f=open('abcFileHandling.txt','r')
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(4))
print(f.tell())



# ---------------------------------------------------
# seek() -- to move cursor (pointer) to a specific position
# f.seek(offset,formware)

data="All students are not bad"
f=open('xyFileHandling.txt','w')
f.write(data)
with open('xyFileHandling.txt','r+') as f:
    text=f.read()
    print(text)
    print("current cursor position:",f.tell())

    f.seek(11)
    print("current cursor position:",f.tell())
    f.write(" GEMS")
    f.seek(0)
    text=f.read()
    print("Data modification.")
    print(text)


# ------------------------------------------------------
# isfile()  -- to check file is available or not in our system
# os.path.isfile(fName)

import os

fName=input("Enter file name:")
if os.path.isfile(fName):
    print("File exist:",fName)
    f= open(fName,'r')
    print("the content of the file is:")
    data=f.read()
    print(data)
    f.close()

else:
    print("File does not exist:",fName)





# ------------------------------------------------------
# wap to print number of lines , words and character present in the given file
# read filename from the keyboard

import os,sys

fName=input("Enter file name:")
if os.path.isfile(fName):
    print("File exist:",fName)
    f= open(fName,'r')
    print("the content of the file is:")

else:
    print("File does not exist:",fName)
    sys.exit(0)

linesCount = wordCount = charCounts = 0
for line in f:
    linesCount = linesCount + 1
    words = line.split()
    wordCount = wordCount + len(words)
    charCounts = charCounts + len(line)

print("The number of line count:", linesCount)
print("The number of words count:", wordCount)
print("The number of character count:", charCounts)

f.close()


# second method ---------------------
import os

fName=input("Enter file name:")
if os.path.isfile(fName):
    print("File exist:",fName)
    f= open(fName,'r')
    print("the content of the file is:")
    linesCount = wordCount = charCounts = 0
    for line in f:
        linesCount = linesCount + 1
        words = line.split()
        wordCount = wordCount + len(words)
        charCounts = charCounts + len(line)

    print("The number of line count:", linesCount)
    print("The number of words count:", wordCount)
    print("The number of character count:", charCounts)

    f.close()

else:
    print("File does not exist:",fName)






#==========================================================================================================
#2. Binary File reading --- image, video, audio
#modes--  rb, wb, ab, r+b, w+b, a+b ,

# for image -----------------------

f1= open("chachu.jpg",'rb')
f2= open("newPick.jpg",'wb')

bytes=f1.read()
f2.write(bytes)
print("New image generated and the name is :newPick.jpg")



# for video -----------------------

f1= open("jk.MP4",'rb')
f2= open("newImage.MP4",'wb')

bytes=f1.read()
f2.write(bytes)
print("New image generated and the name is :newPick.jpg")




# -------------------------------------------------------------------
# Handling CSV file ------
# csv (comma sepreted values) module in the python for handling

import csv

with open("emp.csv",'w',newline='')as f:
    w=csv.writer(f) # returns csv writer object
    w.writerow(["eNO","eNAME","eSALARY","eADDRESS"])
    n=int(input("Enter number of employee:"))
    for i in range(n):
        eNo=int(input("Enter employee number:"))
        eName=input("Enter employee name:")
        eSal=float(input("Enter employee salary:"))
        eAdd=input("Enter employee address:")
        w.writerow([eNo,eName,eSal,eAdd])

print("Total employee data is written in csv file.")



f=open("emp.csv",'r')
r=csv.reader(f) # return reader object
data=list(r)
print(type(data))
print(type(r))

print(data)
for line in data:
    for word in line:
        print(word,"\t",end='')
    print()




# ----------------------------------------------------------------------------------
# zipping and unzipping files ----

# 1. memory utilization improved
# 2. Transport time reduced
# 3. improve performance
# zipfile --module name
# ZipFile -- class name

from zipfile import *
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("abcFileHandling.txt")
f.write("xyFileHandling.txt")
f.close()
print("file created successfully.....")




# -----------------------------------------
# to perform unzip operation
# f=ZipFile("files.zip",'r',ZIP_STORED)

# read and display the content of file


from zipfile import *
f=ZipFile("files.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print("file name:",name)
    print("the content of the file:")
    f1=open(name,'r')
    print(f1.read())
    print()




# ==============================================================================================
# # -------------------------------------------------------------------------------
# working with directories : ---
#  os module

import os

# s1: to know current working directories
cwd=os.getcwd()
print("current working directory:",cwd)

# ---------------------------------------------
# mkdir() -- to create a directory

# s2: to create subdirectory in the current working directory
os.mkdir("mySub")
print("mySub directory is created in cwd.")

# s3: to create subdirectory in the mySub directory
os.mkdir("mySub/mySub1")
print("mySub1 created successfully..")


# makedirs() - to remove multiple directories
# s3: to create multiple sub directory
os.makedirs("sub1/sub2/sub3")
print("directories created successfully..")


# ----------------------------------------------------
# s5: to remove a directory
# rmdir() -- to remove directory

os.rmdir("mySub/mySub1")
print("mySub1 removed or deleted")


# s6: to remove multiple directories
# removedirs() ---

os.removedirs('sub1/sub2/sub3')
print("multiple removed or deleted")




# ------------------------------------------------
# s7: to rename a directory
# rename("old name","new name")

os.rename("mySub","newDir")
print("renamed directory")


# s8: to know content of a directory
# listdir()

print(os.listdir("16module"))
print("task completed")
print()

print(os.listdir(".")) #  .  ==> current working directory


# ---------------------------
# s9: walk() ---
#       os.walk(path,todown=True,onerror=None,followlinks=False)

for dirpath,dirnames,filenames in os.walk("."):
    print("Current working directory path:",dirpath)
    print("directories:",dirnames)
    print("file names:",filenames)
    print()

for dirpath,dirnames,filenames in os.walk("D:/jayvardhan-space/python-durgasir"):
    print("Current working directory path:",dirpath)
    print("directories:",dirnames)
    print("file names:",filenames)
    print()







# ======================================================================================================
# ----------------------------------------------------------------------------------------
#
# os module
# system() -- to execute the system command
os.system("command to execute")



import os
os.system("dir *.py")
os.system("02Datatypes.py")
os. system("04module.py")


# ---------------------------------------
# how to get information about a file
#
# stat() -- function of os

stats=os.stat("xyFileHandling.txt")
print(stats)

# st_mode -- file mode
# st_info -- file information
# st_dev -- device number
# st_nlink -- number of hard link
# st_uid --  user id
# st_gid -- group id
# st_size -- file size
# st_atime -- last access time
# st_mtime -- last modified time
# st_ctime  -- creation time


from datetime import *

stats=os.stat("xyFileHandling.txt")
# print(stats)

print("file size in bytes:",stats.st_size)
print("File last accessed time:",datetime.fromtimestamp(stats.st_atime))
print("File last modified time:",datetime.fromtimestamp(stats.st_mtime))
print("File last creation time:",datetime.fromtimestamp(stats.st_ctime))

print()


