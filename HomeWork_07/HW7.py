phonebook = {"Ivan":"+38056465453","Fedor": "+36535434543","Alex": "+38035431133","Petro Petrovich": "+380679874561","San Sanich": "+380504569874","Dart Weyderovich": "+666666666666","Alesha Popovich": "+345864644847"}
print(phonebook.items())
print(phonebook.values())
print(phonebook.keys())

#show phonebook
stats = phonebook
print(len(phonebook))

#list letter
for lst in phonebook.keys():
    print(list(lst.split()))
#add contact
phonebook["Evgen"] = "+54681444035"
print(phonebook)

#del contact
del phonebook["Ivan"]
print(phonebook)

#show phonebook
for show in phonebook.items():
    print(show)

# contact = input("Enter a contact ")
#
# if phonebook(contact) is None:
#     phonebook["contact"] = "+380"
# print(phonebook.get[contact])


# while True:
#
#     if:
#         name = input("Enter a name ")
#         print(name.split(" "))
#         phone = input("Enter a phone ")
#         print(phone.split("+380"))
#         phonebook[name] = phone
#         print(phonebook)
#     else:
#         print("name in phonebook")






# while True:
#     user_input = input("Enter new contact: ")
#     split_input = user_input.split()
#
#
#     comand = split_input[0]
#     numbers = int(split_input[1])
#     names = split_input[2]
#
#     if user_input.get(phonebook) is None:
#         phonebook[numbers] = 0
#
#     if comand == 'add':
#         phonebook += names
#     elif comand == 'remove':
#         phonebook -= names
#     elif comand == "get":
#         print(phonebook.get(names))
