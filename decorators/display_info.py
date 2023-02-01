
def decorator(original_func):

    def wrapper(*args, **kwargs):
        print("wrapper executed this before {}".format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper


@decorator
def display_info(name, age):
    print("display_info function ran with arguments ({}, {})".format(name, age))


display_info("Mirshod", 24)