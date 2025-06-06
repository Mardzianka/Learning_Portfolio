'''
Program name: Ch 7 Exercise 2.py 
Program to demonstrate the use of a dictionary
The program stores a list of names and telephone extensions
The user can lookup, add, edit or delete a key-value pair,
or print every key value pair in the dictionary
'''

#set up some entries in the dictionary
phoneNums = {
            "Jones, Alan":34,
            "Mills, Dave":21,
            "Harvey, Ron":33,
            "Lansbury, Christine":12
            }
choice = None

while choice != "6":
#print a menu of options
    print("\nMain menu")
    print("1. Look up a telephone number")
    print("2. Add a new name and telephone number")
    print("3. Edit a telephone number")
    print("4. Delete an entry")
    print("5. Print phone directory")
    print("6. Quit")

    choice = input("Enter choice: ")
    print("\n")
        
    if choice == "1":
       name = input("What name? ")
       if name in phoneNums:
          print("Telephone extension is ",phoneNums[name])
       else:
          print("Name not in directory")           

    elif choice == "2":
       name = input ("Enter surname followed by comma, space, first name: ")
       if name not in phoneNums:
          number = input("Enter telephone number: ")
          phoneNums[name] = number
       else:
          print("Name already in directory")
            
    elif choice == "3":
       name =input ("Enter name of person whose phone number you wish to change: ")
       if name in phoneNums:
          number = input("Enter new number: ")
          phoneNums[name] = number
       else:
          print("Name not in directory")

    elif choice == "4":
       name = input("Enter name to delete (Surname, Firstname): ")
       if name in phoneNums:
          del phoneNums[name]
          print ("Name deleted")
       else:
          print("Name not found") 
                     
                        
#print all the key-value pairs in the dictionary
    elif choice == "5":           
#Sort the dictionary before printing,
       print("\nSorted directory\n")
       for name in sorted(phoneNums.keys()):
         print (name, phoneNums[name])
            
    if choice == "6":
       input("Press Enter to exit program: ")
