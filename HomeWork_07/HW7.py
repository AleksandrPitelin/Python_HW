
phonebook = {
        "Aleks": "347638756",
        "Fedor": "3784638754",
        "Den": "2387463745"

    }

while True:
    command = input('Enter a command: ')
    if command == 'list':
        for key in phonebook:
            print(key)
    elif command == 'stats':
        L = phonebook
        print(len(L))
    elif command == 'show':
        s = input("Enter a name: ")
        if phonebook.get(s):
            print(phonebook[s])
    elif command == 'add':
        n = input("Enter a name: ")
        p = int(input("Enter a phone: "))

        if n != phonebook:
            phonebook[n] = p
            print("Contact add to phonebook!")
        else:
            for n, p in phonebook is True:
                print("Contact in phonebook!")
        print(len(phonebook))
        print(phonebook)
    elif command == 'delete':
        n = input("Enter a name: ")
        if phonebook.get(n):
            del phonebook[n]
            print(phonebook)
            print(f"{n} is delete")
    else:
        print("Unknown command!")
