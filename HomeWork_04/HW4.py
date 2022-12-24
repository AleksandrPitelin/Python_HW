# Home Work 5.1

words = input("Enter a text: ")

for letter in words:
    if letter.isupper():
        print("This is a isupper")
    elif letter.islower():
        print("This is a lower")
    elif letter.isdigit():
        if (int(letter)) % 2 == 0:
            print("This is pair digit")
        else:
            print("This is not a pair digit")
    elif letter.isspace():
        print("This is a space")




#---------------------#

# Home Work 5.2

import time

while True:
    text = "I love Python"
    for word in text:
        time.sleep(4.2)
    print(text)
