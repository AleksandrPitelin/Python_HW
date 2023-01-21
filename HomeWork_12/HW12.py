import json



phonebook = {
        "Aleks": "347638756",
        "Fedor": "3784638754",
        "Den": "2387463745"
    }

json_phonebook = json.dumps(phonebook)
print(type(json_phonebook))
print(json_phonebook)

with open("HomeWork_12/Json_hw12", "x") as file_Json:
    file_Json.write(json_phonebook)
