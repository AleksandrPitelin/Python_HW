from datetime import datetime
from time import perf_counter



# def decorator(func):
#     def timer(*args,**kwargs):
#         start = datetime()
#         def inner():
#             return datetime() - start
#         return inner()
#     return timer
def counter(func):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count +=1
        print(f"Функція {func.__name__} викликалась {count} разів")
        return func(*args,**kwargs)
    return inner


@counter
def add(a, b):
    return a + b
add(8,7)
add(5,7)
add(4,6)



# #-----------------------------------------
class MyCustomException(ZeroDivisionError):
    pass
try:
    a = 5/0
    raise MyCustomException("Custom exception is occurred")
except: print("Деление на ноль")





#==========================
class FileManager():
    def __init__(self,f_name,mode):
        self.f_name = f_name
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.f_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager("context.txt","w") as file:
    file.write('==========\nSome code\n==========')

#-----------------------------

#
class MyContext:

    def __enter__(self):
        print('==========')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print(exc_val)
        print('==========')
        return True