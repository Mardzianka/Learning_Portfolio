#Program name: Ch 6 Exercise 5 Caesar Cipher.py
#Program to encrypt a password using Caesar cipher
#Test by entering BENXY3

storedPassword = "EHQAB6"
passwordOK = False
tries = 0

while not passwordOK and tries < 3:
    password = input("Please enter your password: ")
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
        print("Password incorrect ")
        tries +=1

if not passwordOK:
    print("\nSorry, your password is not accepted.")
input ("\nPress Enter to exit ")
