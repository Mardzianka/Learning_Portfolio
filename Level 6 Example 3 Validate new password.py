#Program name: Level 6 Example 3 Validate new password

print("Your password must be at least 10 characters long")
print("It must contain at least one uppercase and one lowercase letter")

validPassword = False

while not validPassword:
    validPassword = True
    password = input("Please enter password: ")
    if len(password) < 10:
        validPassword = False
        print("Must be at least 10 characters")
    elif password.isupper():
        validPassword = False
        print("Must contain at least one lowercase letter")
    elif password.islower():
        validPassword = False
        print("Must contain at least one uppercase letter")
    if not validPassword:
        print("Invalid password")
    
        
print("Valid password entered")
