class class_decorator:

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@class_decorator
def display_info(name, age):
    print("display_info function ran with arguments ({}, {})".format(name, age))


display_info("John", 33)
