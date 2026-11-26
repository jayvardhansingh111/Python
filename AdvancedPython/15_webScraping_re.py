# Web Scraping using regular expression :

# urllib : module


import re
import urllib.request

sites=['https://google.com','https://rediff.com','https://instagram.com']

for s in sites:
    print('Searching...',s)
    u=urllib.request.urlopen(s)
    text = u.read()
    title=re.findall("<title>.*</title>",str(text),re.I)
    print(title[0])




import re
import urllib.request

sites=['https://google.com']

for s in sites:
    print('Searching...',s)
    u=urllib.request.urlopen(s)
    text = u.read()
    title=re.findall("<title>.*</title>",str(text),re.I)
    print(title[0])
    # print(text)
    print(type(text))








# --------------------------------------------------------------------------------
# write a program to read all the mobile numbers from the redBus.com

import  re
import urllib.request

url=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=url.read()
# numbers=re.findall('[0-9-]{7}[0-9-]',str(text),re.I)
# numbers=re.findall('[0-9]{3}[-][0-9]{8}',str(text),re.I)
# numbers=re.findall('[0-9]{9}',str(text),re.I)
numbers=re.findall('[0-9]{6}',str(text),re.I)


for n in numbers:
    print(n)





# --------------------------------------------------------------------------------
# to check mail id is valid or not

# jay123@gmail.com


import re

s=input('Enter mail id: ')
# mail=re.fullmatch('[a-zA-Z0-9]*@gmail[.]com',s)
mail=re.fullmatch('[a-zA-Z0-9]*@(gmail|yahoo)[.][a-z]',s)


if mail != None:
    print(s,': is valid mail id')
else:
    print(s,': invalid mail id')






# --------------------------------------------------------------------------------
# check car registration number is valid or not

# TS07EA7777
#              TS[0-2][0-9][A-Z]{2}\d{4}

import re

s=input('Enter car number: ')
car_registration_number=re.fullmatch(r'TS[0-2][0-9][A-Z]{2} \d{4}',str(s),re.I)

if car_registration_number != None:
    print(s,': is valid car number')
else:
    print(s,': invalid car number')


