
text = int(input("Enter a digit: "))
def my_generator():
    f1, f2 = 0, 1
    for i in range(text):
        print(f1, end=" ")
        f1, f2 = f2, f1 + f2
    yield i

gen = my_generator()
print(next(gen))

