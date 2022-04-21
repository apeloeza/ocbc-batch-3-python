#Generator

def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

my_generator()

"""In the above example we create a simple generator using the yield statements. We can use it in a for loop just like we use any other iterators."""

for char in my_generator():
  print(char)

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i, end=' ')

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
  print(i, end=" ")

"""Understanding Generators
So far, you’ve learned about the two primary ways of creating generators: by using generator functions and generator expressions. You might even have an intuitive understanding of how generators work. Let’s take a moment to make that knowledge a little more explicit.
Generator functions look and act just like regular functions, but with one defining characteristic. Generator functions use the Python yield keyword instead of return. Recall the generator function you wrote earlier:
```py
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```
This looks like a typical function definition, except for the Python yield statement and the code that follows it. yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
Instead, the state of the function is remembered. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again. Since generator functions look like other functions and act very similarly to them, you can assume that generator expressions are very similar to other comprehensions available in Python.
**Functions**
Before you can understand decorators, you must first understand how functions work. For our purposes, a function returns a value based on the given arguments. Here is a very simple example:
```py
>>> def add_one(number):
...     return number + 1
>>> add_one(2)
3
```
## First-Class Objects
In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). Consider the following three functions:
"""
