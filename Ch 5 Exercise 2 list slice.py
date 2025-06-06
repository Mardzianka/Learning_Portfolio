#Program name: Ch 5 Exercise 2 list slice.py
#Program appends names entered by user to a list
#Slices the list in half and prints the first half of the list

nameList = []

name = input("Enter name: ")
while name.lower() != "end":
    nameList.append(name)
    name = input("Enter next name, 'end' to finish: ")
midpoint = len(nameList)//2
newList = nameList[0:midpoint]
print(newList)

input("Press Enter to exit")
