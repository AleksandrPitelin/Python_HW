from datetime import datetime
from time import perf_counter



def decorator(func):
    def timer():
        start = perf_counter()
        def inner():
            return perf_counter() - start
        return inner

def counter(func):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count +=1
        print(f"Функція {func.__name__} викликалась {count} разів")
        return func(*args,**kwargs)


@counter
@decorator
def add(a, b):
    a = int(input("first digit "))
    b = int(input("twice digit "))
    return a + b




# #-----------------------------------------
def MyCustomException(Exception):
    pass
try:
    a,b/0
except:
    MyCustomException
    print("Custom exception is occured")

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

while True:
    b = "HelloWorld!"
    a = input("Enter value: ")
    try:
        a=a*10
        res = a + b + a
        print(res)

    except (TypeError):
        print("Custom exception is occured")
    except (KeyboardInterrupt):
        print("KeyboardInterrupt")
    else:
        pass
    finally:
        pass