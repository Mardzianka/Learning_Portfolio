#Program name: Ch 15 Exercise 2 with errors.py
#Program to encrypt a password entered by user using Caesar cipher
#and compare with stored encrypted password
#For test purposes enter a password BENXY3 as a correct password,
#or anything else to test incorrect password

storedPassword = "EHQAB6"
passwordOK = False

password = input("Please enter your password: ")
while not passwordOK:
    codedPassword = ""
    for num in range(len(password)):
        asciiValue = ord(password[num])
        codedValue = asciiValue + 3
        if codedValue > ord("X"):
            codedValue -= 26
        codedPassword = codedPassword + chr(codedValue) 

    if storedPassword == codedPassword:
        print("Password accepted")
        passwordOK = True
    else:
        password =input("Password incorrect - please re-enter: ")
        
input ("\nPress Enter to exit ")
