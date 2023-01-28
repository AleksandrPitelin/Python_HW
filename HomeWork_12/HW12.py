import json
from datetime import datetime
def timer():
    start = datetime()
    def inner():
        return datetime() - start
    return inner

def funcname(func):
    def inner(*args,**kwargs):
        print(f"Функція {func.__name__}")
        return func(*args,**kwargs)





# phonebook ={
#         "Aleks": "347638756",
#         "Fedor": "3784638754",
#         "Den": "2387463745"
#
#      }
# json_phonebook = json.dumps(phonebook)

try:
    with open("/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_12/Json_hw12", 'r') as file:
        data = file.read()
        phonebook = json.loads(data)
except FileNotFoundError:
    phonebook = {}


while True:
    # @timer(command)
    # @funcname(command)
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

        # if n != phonebook:
        #     phonebook[n] = p
        if n not in phonebook:
            phonebook[n] = p
            with open("/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_12/Json_hw12", 'w+') as file_json:
                content = json.dumps(phonebook)
                file_json.write(content)
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
#======================================#
