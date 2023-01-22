text = int(input("Enter a digit: "))
def my_generator(some_text):
    f1, f2 = 0, 1
    for fib in range(some_text+1):
        yield f1
        f1, f2 = f2, f1 + f2

gen = my_generator(text)
n=0
for value in gen:
    if n == text:
        print(value)
    n += 1
