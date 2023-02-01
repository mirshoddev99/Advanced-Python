# Python program showing
# file management using
# context manager


class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with ContextManager() as manager:
    print('with statement block')

"""
In this case, a ContextManager object is created. This is assigned to the variable after the keyword i.e manager. 
On running the above program, the following get executed in sequence:

__init__()
__enter__()
statement body (code inside the with block)
__exit__()[the parameters in this method are used to manage exceptions]
"""
print()


class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)
print()
"""
  File management using context manager and with statement: On executing the with block, the following operations happen in sequence:

A FileManager object is created with test.txt as the filename and w(write) as the mode when __init__ method is executed.
The __enter__ method opens the test.txt file in write mode(setup operation) and returns a file object to variable f.
The text ‘Test’ is written into the file.
The __exit__ method takes care of closing the file on exiting the with block(teardown operation). 
When print(f.closed) is run, the output is True as the FileManager has already taken care of closing the file which otherwise needed to be explicitly done.
"""
