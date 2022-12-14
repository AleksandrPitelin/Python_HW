def question():
    while True:
        name = input("Назовите Ваше имя ")
        try:
            number = int(input("Сколько вам лет? "))
        except: ValueError
            print("Error! Это не число, попробуйте снова.")
        else:
             print("Круто, ", name, "! ,это", len(name), "букв , Вам", number*12,"Месяцев,Это", number*12%2, "число")
             break
question()



#str_or_int = input("Enter a text ")

#if str_or_int == int:
#    print(int("This is int"))
#else:
#    print(str("This is str"))



#input("ENTER a text ")

#if input("Enter a text"):
#print("This is a integer")
#else input() == str:
#print("This is a string")

#len_of_the_text = len(input())
#print(len_of_the_text)

#name = input("What's your name?" + " ")
#print('Hello', name, "!")
#age = int(input("How old are you?"))
#print(age)