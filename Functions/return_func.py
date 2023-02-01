"""3. Functions can return another function: Because functions are objects we can return a function from another function.
In the below example, the create_adder function returns adder function."""


# Python program to illustrate functions
# Functions can return another function

# def create_adder(x):
#     def adder(y):
#         return x + y
#
#     return adder
#
# # the first way
# add_15 = create_adder(15)(25)
# print(add_15)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


# the second way
add_15 = create_adder(15)
print(add_15(25))

"""
This is called Higher Order Function (HOF)
"""


