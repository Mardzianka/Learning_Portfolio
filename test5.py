#create a program that declares the following variables
#name david
#weight 88.4
#birth year 1997
#create a variable called id card and add the following data
#name
#weight as whole number
#age
#birth year
#display information 

name = 'David'
weight = 88.4
birth_year = '1997'
age = 2024 - int(birth_year)
weight = int(weight)
ID_card = "Name: " + name + "\n"
ID_card = ID_card + "Age: " + str(age) + "\n"
ID_card = ID_card + "Birth year: " + birth_year + "\n"
ID_card = ID_card + "Weight: " + str(weight) + "\n"

print(ID_card)


