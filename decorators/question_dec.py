
def my_decorator(func):

    def wrapper():
        print("Do you want to get messages?")
        msg = input("enter yes (y) - no (n): ")
        if msg == "y":
            func()
        else:
            print("You did not want to get messages! Sorry")
    return wrapper


@my_decorator
def question():
    print("I get messages through email!")


question()