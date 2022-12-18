some_text = input("Enter a text: ")
if some_text.isalpha():
    print(len(some_text))
    print("have len,this is a string")
elif some_text.isdigit():
    if (int(some_text)) % 2 == 0:
        print("This is a digit")
    else:
        print("This is not a digit")
