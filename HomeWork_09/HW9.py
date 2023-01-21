text = int(input("Enter a digit: "))
def my_generator():
    f1, f2 = 0, 1
    for fib in range(text):
        yield fib
        f1, f2 = f2, f1 + f2

gen = my_generator()
n=0
for value in gen:
    if n== int(text):
        print(value)
        break