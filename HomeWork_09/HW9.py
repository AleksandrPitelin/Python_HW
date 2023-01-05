text = int(input("Enter a digit: "))

def my_generator(text):
    values = range(int(text))
    for value in values:
        yield value

generator = my_generator(text)
for item in generator:
    print(item)

f1, f2 = 0, 1
for _ in range(text):
    print(f1, end=" ")
    f1, f2=f2, f1+f2