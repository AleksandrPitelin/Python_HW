import re
import json
from datetime import datetime


try:
    with open('Json_hw14', 'r') as file:
        data = file.read()
        phonebook = json.loads(data)
except FileNotFoundError:
    phonebook = {}

while True:
    command = input('Enter a command: ')
    if command == 'list':
        for key in phonebook:
            print(key)
    elif command == 'stats':
        print(len(phonebook))
    elif command == 'show':
        s = input("Enter a name: ")
        if phonebook.get(s):
            print(phonebook[s])
    elif command == 'add':
        n = input("Enter a name: ")
        p = int(input("Enter a phone: "))
        tel = re.search(r"^(\+380|380|0)[0-9]{9}$", p)
        if tel is not None:
            if n not in phonebook:
                phonebook[n] = p
                with open("Json_hw14", 'w+') as file_json:
                    json_phonebook = json.dumps(phonebook)
                    file_json.write(json_phonebook)
                    print('Phone number added successfully')
            else:
                print('Name already exists')
        else:
            print('Invalid phone number')

    elif command == 'delete':
        n = input("Enter a name: ")
        if phonebook.get(n):
            del phonebook[n]
            with open("Json_hw14", 'w+') as file_json:
                json_phonebook = json.dumps(phonebook)
                file_json.write(json_phonebook)
            print(phonebook)
            print(f"{n} is delete")
    else:
        print("Unknown command!")