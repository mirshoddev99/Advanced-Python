"""2. Functions can be passed as arguments to other functions: Because functions are objects we can pass them as arguments to other functions.
Functions that can accept other functions as arguments are also called higher-order functions.
In the example below, we have created a function greet which takes a function as an argument."""


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)