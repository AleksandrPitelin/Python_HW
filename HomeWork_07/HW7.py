
phonebook = {
        "Aleks": "347638756",
        "Fedor": "3784638754",
        "Den": "2387463745"

    }


if input("If you wont add - Enter 'add'") == "add":

    n = input("Enter a name: ")
    p = int(input("Enter a phone: "))

    if n != phonebook:
        phonebook[n] = p
        print("Contact add to phonebook!")
    else:
        for n,p in phonebook is True:
            print("Contact in phonebook!")
    print(len(phonebook))
    print(phonebook)
elif input("If you wont del - Enter 'delete'") == "delete":
    n = input("Enter a name: ")
    if phonebook.get(n):
        del phonebook[n]
        print(phonebook)
        print(f"{n} is delete")
elif input("If you wont see a list - Enter a 'list' ") == "list":
    for key in phonebook:
        print(key)
elif input("If you wont see a stats - Enter a 'stats' ") == "stats":
        L = phonebook
        print(len(L))
elif input("If you wont see a show - Enter a 'show' ") == "show":
    s = input("Enter a name: ")
    if phonebook.get(s):
        print(phonebook[s])
else:
        print("Unknown command!")