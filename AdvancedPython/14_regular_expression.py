# Regular Expression  -- if we want to represent a group of string according to a particular
#                        format / pattern .

#  ctrl + f  --> for searching the element in code

# module --  re ( regular expression )

import re

# 1. compile() -- to compile a pattern into RegexObject

pattern=re.compile('Python')


# 2. finditer() --- return an iterator which yields match obj for every match
#
matcher=pattern.finditer('p')
print(matcher)

#          1. start()  -- return start index
#          2. end()   ---  return end+1 index
#          3. group()  -- returns match string




count=0
pattern=re.compile('ab')
# pattern=re.compile('bb')
# pattern=re.compile('ba')
# pattern=re.compile('aa')

matcher=pattern.finditer('abaababa')
for mach in matcher:
    count +=1
    print(mach.start(),'...',mach.end(),'...',mach.group())
print('The number of occurrences:',count)






# -------------------------------------------------------------
# character classes: - use to search a group of characters


# [abc]  -- either a or b or c
# [^abc]  -- except a and b and c
# [a-z]  -- any lowercase alphabet symbol
# [A-Z]  -- any uppercase alphabet symbol
# [a-zA-Z]  -- any  alphabet symbol
# [0-9]   --- any digit between 0 and 9
# [a-zA-Z0-9]  -- any alphabet
# [^a-zA-Z0-9] -- Special characters

import re
matcher=re.finditer('[x]','a7b@k9xz')
for m in matcher:
    print(m.start(),'...',m.group())

matcher=re.finditer('[abc]','a7b@k9xz')
for m in matcher:
    print(m.start(),'...',m.group())

matcher=re.finditer('[0-9]','a7b@k9xz')
for m in matcher:
    print(m.start(),'...',m.group())

matcher=re.finditer('[^a-zA-Z0-9]','a7b@k9xz')
for m in matcher:
    print(m.start(),'...',m.group())



# -------------------------------------------------------------
# predefined character classes -

# \s -- space character
# \S -- except space character
# \d -- any digit
# \D -- except digit
# \w -- any word character (alpha numeric )
# \W -- special characters
# .  --> every character


import re
matcher =re.finditer(r'\s','a7bdhjn 6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"\S",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"\w",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"\W",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())


import re
matcher =re.finditer(r"\d",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"\D",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())




import re
matcher =re.finditer(r".",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())



# # -------------------------------------------------------------------
# Quantifiers  : -- to specify the number of occurrence to match

# a  -> Exactly one 'a'
# a+  -> At least one 'a'
# a*  -> any number of a`s including zero number also
# a?  -> at most one 'a' ,or zero
# a{m} -> exactly m number of a`s
# a{m,n} -> min m number of a`s and max n number of a`s



import re
matcher =re.finditer(r"a",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"a+",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"a*",'a7bdhjn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"a?",'a7bdajn6xds9&')
for m in matcher:
    print(m.start(),'...',m.group())


import re
matcher =re.finditer(r"a{2}",'a7bdahjn6xdaas9&aa')
for m in matcher:
    print(m.start(),'...',m.group())

import re
matcher =re.finditer(r"a{2,3}",'a7aabdahjna6xaaads9&')
for m in matcher:
    print(m.start(),'...',m.group())


# ^a  -- except a every thing
import re
matcher =re.finditer(r"[^a]",'a7aabdahjna6xaaads9&')
for m in matcher:
    print(m.start(),'...',m.group())


# # a$  -- ends with of the char or not
import re
matcher =re.finditer(r"a$",'a7aabdahjna6xaaads9&')
for m in matcher:
    print(m.start(),'...',m.group())





# # -------------------------------------------------------------------
# important function of re module --

# 1. match()   -- to check the given pattern at beginning or not (if match then Match obj otherwise None)
# 2. fullmatch  --- check the complete string match or not
# 3. search()  -- to search entire string
# 4. findall()   -- to find all occurrence of the match , return matches in list
# 5. finditer()  -- it returns iterator of matched objects
# 6. sub() ---     replacement
# 7. subn()  --- return the number of replacements
# 8. split()  --- to split the string according to a pattern
# 9. compile()



# 1. match()   -- to check the given pattern at biginning or not (if match then Match obj otherwise None)

import re
s=input("Enter pattern to check:")
m=re.match(s,"asvbyn")
if m!=None:
    print("match is available at the beginning of the string")
    print("Start index:{}, End index:{}".format(m.start(),m.end()))
else:
    print("match is not available in string")




# 2. fullmatch  --- check the complete string match or not

import re
s=input("Enter pattern to check:")
m=re.fullmatch(s,"asvbyn")
if m!=None:
    print("match is available at the beginning of the string")
    print("Start index:{}, End index:{}".format(m.start(),m.end()))
else:
    print("match is not available in string")




# 3. search()  -- to search entire string

import re
s=input("Enter pattern to check:")
m=re.search(s,"asvbyn")
if m!=None:
    print("match is available at the beginning of the string")
    print("Start index:{}, End index:{}".format(m.start(),m.end()))
else:
    print("match is not available in string")




# 4. findall()  -- to find all occurrence of the match

import re
m=re.findall('[0-9]',"asv2354b53yn")
print(m)

import re
m=re.findall('\W',"a7# 46#$6b53yn")
print(m)



# 5. finditer()  -- it returns iterator of matched object

import re
itr=re.finditer('[a-z]',"asv2354b53yn")
for m in itr:
    print(m.start(),'....',m.end(),'...',m.group())


import re
itr=re.finditer('\d',"asv2354b53yn")
for m in itr:
    print(m.start(),'....',m.end(),'...',m.group())



# 6. sub()  -- replacement
# re.sub(regex,replacement,target_string)

import re
s=re.sub(r'\d','#','a7bdh4jd8cj3')
print(s)

import re
s=re.sub(r'\d','aaa','a7bdh4jd8cj3')
print(s)


# 7. subn() -- to know number of replacements
# (result_string,number of replacement)


import re
s=re.subn(r'\d','#','a7bdh4jd8cj3')
print(type(s))
print("The result string:",s[0])
print("The number of replacement :",s[1])




# 8. split()  -- to split the string according to a pattern

import re
l=re.split(r'-','10-20-30-04-40-50-66')
print(l)


s=re.split(r'\.','www.jayve@.com')
for i in s:
    print(i)

s=re.split(r' ','www.jayve@.com')
for i in s:
    print(i)

#9. compile()








# --------------------------------------------------------------------

# ^symbol : starts with -- it checks the pattern st starting match or not

import re

s='Learning python is very easy'
res=re.search("^Learn",s)
if res != None:
    print("Target string starts with  earn")
else:
    print('Target string not starts with Learn')





# $ symbol : ends with -- check pattern in the ending
s='Learning python is very easy'
res=re.search("easy$",s)
if res != None:
    print("Target string ends with  easy")
else:
    print('Target string not ends with easy')


s='Learning python is very easy'
res=re.search("Easy$",s)
if res != None:
    print("Target string ends with  easy")
else:
    print('Target string not ends with easy')


s='Learning python is very easy'
res=re.search("Easy$",s,re.IGNORECASE)
if res != None:
    print("Target string ends with  easy")
else:
    print('Target string not ends with easy')










# -------------------------------------------------------------------------------------------

# ques1. ALl yava language identifiers

# 1. The allowed characters are
#     alphabets , digits, #

# 2. first character should be lowercase alphabet from a to z

# 3. the second charactor should be any digit and divisible by 3
# 4. the length of identifier should be between at least 2



import re
s=input('Enter the identifier to check: ')
m=re.fullmatch('[a-z][0369][a-zA-Z0-9#]',s)

if m != None:
    print(s,' is valid identifier')
else:
    print(s,' is not valid identifier')








# ques2. 10 digit mobile number

# [6789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
# [6789][0-9]{9}
# [6-9]\d{9}

import re
s=input("Enter mobile number:")
m=re.fullmatch(r'[6-9]\d{9}',s)
if m != None:
    print(s,' is valid mobile number')
else:
    print(s,' is not valid mobile number')











# -------------------------------------------------------------------
# ques write a program to extract mobile number from the file



import re

f1 = open('abc.txt', 'r')
f2 = open('output.txt', 'w')

for line in f1:
    list1 = re.findall(r'[6-9]\d{9}', line)

    for number in list1:
            f2.write(number + '\n')

print("Extracted all mobile numbers in output.txt")

f1.close()
f2.close()




