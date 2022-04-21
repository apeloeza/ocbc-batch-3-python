# Intro to decorator

def say_hello(name):            # 4
    return f"Hello {name}"      # Hello Bob
 
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"
 
def greet_bob(greeter_func):    # 2
    return greeter_func("Bob")  # 3 say_hello("Bob")
 
print( greet_bob(say_hello) ) # 1

print('============================')

def say_hello(name):
    return f"Hello {name}"
 
def be_awesome(name):           # 3
    return f"Yo {name}, together we are the awesomest!" # 4 print ini
 
def greet_bob(greeter_func):    # 2
    return greeter_func("Bob")  # be_awesome("Bob")
 
print( greet_bob(be_awesome) )  #1

# Inner Function
def parent():
    print("Printing from the parent() function")  # 1
 
    def first_child(): # 6
        print("Printing from the first_child() function") # 7
 
    def second_child(): # 3
        print("Printing from the second_child() function") #4
 
    second_child()  # 2
    first_child()   # 5
 
parent()

# Returning functions from functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
    
first = parent(1)
# print(first)
print(first())

# Simple Decorators
def my_decorator(func):             # 2 func = say_whee
    def wrapper():                  # 6 karena ini <function my_decorator.<locals>.wrapper at 0x000001B515E5F160>
        print("Something is happening before the function is called.") # 7
        func()                      # 8 say_whee()
        print("Something is happening after the function is called.") #9
    return wrapper                  # 3
 
def say_whee():                     # 9
    print("Whee!")                  # 10
    print("me e  e e e!")
    
say_wheezz = my_decorator(say_whee) # 1
print(say_wheezz)                   # 4 <function my_decorator.<locals>.wrapper at 0x000001B515E5F160>
 
say_wheezz()                        #5

print('============================')

def my_decorator(func): # 4
    def wrapper():  # 6
        print("Something is happening before the function is called.") # 7
        func() # 8
        print("Something is happening after the function is called.") # 10
    return wrapper #5
 
@my_decorator   # 3
def say_whee(): # 2 #9
    print("Whee!")  #9
 
# say_whee = my_decorator(say_whee)
print(say_whee)
say_whee() # 1

print('============================')