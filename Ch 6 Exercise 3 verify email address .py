#Program name: Ch 6 Exercise 3.py
#verifies an email address

validEmail = None

while not validEmail:
    email = input("Enter your email address: ")
    email2 = input ("Confirm you email address by entering it again: ")
    if email == email2:
        print("\nemail accepted")
        validEmail = True
    else:
        print("These do not match - please re-enter: ")
        
input("Press Enter to exit ")