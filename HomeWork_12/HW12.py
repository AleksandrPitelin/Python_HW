import json



phonebook = {
        "Aleks": "347638756",
        "Fedor": "3784638754",
        "Den": "2387463745"

    }
# with open("HomeWork_12/HW12.py", "w")

json_phonebook = json.dumps(phonebook)
print(type(json_phonebook))