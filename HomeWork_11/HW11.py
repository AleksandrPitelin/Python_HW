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
@decorator
@counter
a = int(input("first digit "))
b = int(input("twice digit "))
def add(a, b):
    return a + b
add = decorator(add)
add2 = counter(add)
print(add)
print(add2)

#-----------------------------------------
try:
    a,b/0
except:
    MyCustomException=(Exception)
    print("Custom exception is occured")


#==========================

with open("context.txt","w") as file:
    file.write('==========\nprint(HelloWorld!)\n==========')
print(file)

#-----------------------------


while True:
    b = "HelloWorld!"
    a = input("Enter value: ")
    try:
        a=a*10
        res = a + b + a

    except (TypeError):
        print("Custom exception is occured")
    except (KeyboardInterrupt):
        print("KeyboardInterrupt")
    else:
        print("else compleat")
    finally:
        pass
    print(res)