#I love Python*42#

# Zadanie 1
print("I love Python "*42)

#age_in_month#

# Zadanie 2
month = 12
age_in_year = 37
age_in_month = age_in_year * month
print(age_in_month)

#Take age in "y" Zadanie 2#

# Zadanie 3
age_in_years = age_in_month//12
print (age_in_years)

#----------------------#
# Zadanie 4
first_name = "Oleksandr"
last_name = "Pitelin"
full_name = first_name +" "+ last_name
result = "Му name is" +" "+ full_name + " I’m " + str(age_in_years) + " years old"
print(result)

#----------------------#
# Zadanie 5

a=5>7
print(a)

a=4<=4
print(a)

a=52//2<14*2
print(a)

a=51
print(a>31 and a<55)

a=12/3>2*7
print(a)


#insert (int) to  (str)#
# Zadanie 6
a = 2
b = 5
c = 6
d = str(a)+str(b)+str(c)
print(d)
