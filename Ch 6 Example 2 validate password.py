#Program name: Ch 6 Example 2 validate password.py
#program to check that a password contains an uppercase letter

print("Password must contain at least one uppercase letter")
password = input("Please enter new password: ")
passwordValid = False
while not passwordValid:
    for index in range(len(password)):
        if ord(password[index]) in range(65,91):
            passwordValid = True
    if not passwordValid:
        password = input("Invalid - please enter new password: ")
print ("Password accepted")

input ("\n Press Enter to continue ")
