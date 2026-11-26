#  ''' this is doc string '''



# # various methods in math module
# import math
#
# print(dir(math))
# help(math)





'''
    This is a test module use for test the module documentation
    and written for the learner can learn from it '''

__author__ = 'Jay'
__copyright__ = 'Copy Right by Jay'

def add(a,b):
    ''' This is an arithemetic function which adds two variables '''
    return a+b

def multiply(a,b):
    ''' This is an arithemetic function which multiply two variables '''
    return a*b

def main():
    ''' This is a main function which prints the values '''
    print('Sum :',add(4,5))
    print('Product :',multiply(4,5))

x=333
y=555


if __name__ == '__main__':
    main()








# ===========================================================================

# Pydoc  ==>> Python Documentation Tool

# python -m pydoc math
# python -m pydoc [any module name ]

#  python -m pydoc   ---> for pydoc names modules

# python -m pydoc -p [port number]  --> for seeing documentation in web



 # python -m pydoc -w math  ---> writing the module in the html file
# wrote math.html










