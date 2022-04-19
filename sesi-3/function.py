#example of function creation
from re import M
from tkinter import Variable


def my_function(p, l):
    '''Function to calculate area of square'''
    print(p * l)

def printme(str_input):
    '''This prints a passed string into this function'''
    print(str_input)

# calling a function
def printme(str_input):
    '''This prints a passed string into this function'''
    print(str_input)

# #now you can call printme function
printme(" I'm first call to user defined function!")
printme("Again second call to the same function")

#function devinition is here
def changeme( mylist ):
    '''This chalange a passed list into this function'''
    mylist = mylist+[1,2,3,4]
    print("\nValues inside the function : ", mylist)
    return

#now you can call changeme function
mylist = [10,20,30]
print("nValues outside the function - before : ",mylist)
mylist=changeme( mylist )
print("\nValues outside the function - after : ", mylist)

#function devinition is here
def changeme ( mylist ):
    '''This changes a passed lisst into this function'''
    mylist = [1,2,3,4] #this would assign new reference in my list
    print("Values inside the function : ", mylist)

#now you can call changeme function
mylist = [10,20,30]
changeme( mylist)
print("values outside the function : ", mylist)
print("")

#function definition is here
def printme( str_input ):
    '''This prints a passed string into this function'''
    print(str_input)
    print("")

#now you can call printme function
printme("hello")

# # this syntax will give you an error
#printme()

# function definition is here
def calculate_rect(length, width):
    '''This function is used to calculate area of rectangle'''
    print('area :', length*width)
    print("")

#define parameters
length = 100
width = 20

#call calculate_rect
calculate_rect(length, width)

# # this syntax will give you an error
# calculate_rect(length)

# function definition is here
def printme( str_input ):
    '''This prints a passed string into this function'''
    print(str_input)
    print("")

# now you can call printme function
printme(str_input = "Hactiv8")
print("")

#function definition is here
def printinfo( name, age):
    '''This prints a passed info into this function'''
    print("Name : ", name)
    print("Age : ",age)
    print("")

#now you can call printinfo function
printinfo( age=4, name="a")
print("")

#default Arguments
#function definition is here
def printinfo( name, age = 26):
    '''Thid prints a passed info into this function'''
    print("Name : ", name)
    print("Age : ",age)
    print("")

# now you can call printinfo function
printinfo ( age=50, name="hactiv8")
printinfo( name="hactiv8")

#function definition is here
def printinfo(name,age=26):
    '''This prints a passed info into this function'''
    print("Name : ", name)
    print("Age : ", age)
    print("")

#now you can call printinfo function
printinfo( age=50, name="Hactiv8")

#variabel argument
#function definition is here
def printinfo(arg1,*vartuple):
#dev print info(arg1, arg2, arg3, arg4):
    '''This prints a variable passed arguments'''
    print('arg1     : ', arg1)
    print('vartuple : ', vartuple)
    print("")

    for var in vartuple:
        print('isi vartuple : ', var)

#now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a")

#variable-length Argument have two types
#create a funcction with nonkeyword variables
def person_car(total_data, **kwargs):
    '''Create a function to print who owns what car'''
    print('Total Data : ', total_data)
    for key, value in kwargs.items():
        print('Person   : ', key)
        print('Car      : ', value)
        print("")

person_car(3, jimmy='chevrolt', frank='ford', tina='honda')
person_car(3)

# parameters (jimmy='chevrolet', frank='ford', tina='honda') will be equal to
# kwargs ={
#     'jimmy' : 'chevrolet',
#     'frank' : 'ford',
#     'tina'  : 'honda'
# }

#the annonymous functions
#function definition is here 
sum = lambda arg1, arg2: arg1 + arg2

# that lamda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

#now you can call su as a function
print("value of total : ", sum( 10,20 ))
print("value of total : ", sum( 20,20 ))
print("")

#the return statement
#function definition is here
def sum(arg1, arg2 ):
    # Add both the parameters and return them.
    total = arg1 + arg2
    return total
#now you can call sum dunction
total = sum(10, 20)
print("Result function : ", total)
print("")

# scope of variables
# declare a global Variable
total = 0

# create sum function
def sum (arg1,arg2):
    total = arg1 + arg2;
    print("Inside the function local total  : ",total)

#call a function
sum( 10,20 )
print("Outside the function global total    : ", total)
print("")
#declare a global variable
total = 0

# create sum function
def sum( arg1, arg2 ):
    total = arg1 + arg2;
    print("Inside the function local total   : ", total)
    return total

# call a function
print("Outside the function global total - before   : ", total)
total = sum( 10,20 )
print("Outside the function global total - after    : ",total)

# Docstring
#example of the docstring in a function
def sum_number(number1, number2):
    '''
    This function is used to sum of 2 variables.
    :param num1: Input number 1 | in or float
    :param num2: Input number 2 | in or float

    return: num3: Sum of nuber | int or float
    '''

    num3 = number1 + number2
    return num3

#syntax to get explanation/docstring from a perticular module/function/class
print(sum_number.__doc__)
