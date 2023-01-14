
text = int(input("Enter a digit: "))
def my_generator():
    f1, f2 = 0, 1
    for my_generator in range(text):
        yield
        print(f1,end=" ")
        f1, f2 = f2, f1 + f2


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))