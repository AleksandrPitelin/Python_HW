import re
import json
from datetime import datetime


try:
    with open('/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_14/Json_hw14', 'r') as file:
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
        tel = re.search(r"(\+?3?8?0)(\d+)", p)
        if p in tel:
            print("Ok")
        else:
            print("Enter valid number")

        if n not in phonebook:
            phonebook[n] = p
            with open("/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_14/Json_hw14", 'w+') as file_json:
                json_phonebook = json.dumps(phonebook)
                file_json.write(json_phonebook)

        else:
            print("Unknown command!")

    elif command == 'delete':
        n = input("Enter a name: ")
        if phonebook.get(n):
            del phonebook[n]
            with open("/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_14/Json_hw14", 'w+') as file_json:
                json_phonebook = json.dumps(phonebook)
                file_json.write(json_phonebook)
            print(phonebook)
            print(f"{n} is delete")
    else:
        print("Unknown command!")