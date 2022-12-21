from datetime import time
#---------------------#
# Home Work 1

words = input("Enter a text: ")

for letter in words:
    if letter.istitle():
        print("This is a title")
    elif letter.islower():
        print("This is a lower")
    elif letter.isdigit():
        if (int(letter)) % 2 == 0:
            print("This is a digit")
        else:
            print("This is not a digit")
    elif letter.isspace():
        print("This is a space")




#---------------------#
# Home Work 2


import time

text = "I love Python"
for word in text:
    time.sleep(4.2)
    print(text)
