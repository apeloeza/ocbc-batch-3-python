#intro to declarator

# def say_hello(name):
#     return f"Hello{name}"

# def be_awesome(name):
#     return f"Yo {name}, Together we are the awesome"

# def greet_bob(greater_func):
#     return greater_func("Bob")


def say_hello(name):
    return f"Hello{name}"

def be_awesome(name):           #3
    return f"Yo {name}, Together we are the awesome"    #4 print ini

def greet_bob(greeter_func):    #2 
    return greeter_func("Bob")  #be_awesome

greet_bob