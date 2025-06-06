#Program name: Ch 6 Exercise 4 validate password.py
#validates a new password

ucaseLetters = ["A","B","C","D","E","F","G","H","I",\
                "J","K","L","M","N","O","P","Q","R",\
                "S","T","U","V","W","X","Y","Z"]

#define the lowercase letters
lcaseLetters=[]
for letter in ucaseLetters:
    lcaseLetter = letter.lower()
    lcaseLetters.append(lcaseLetter)
#print(lcaseLetters)

numbers = ["0","1","2","3","4","5","6","7","8","9"]

print ("""Your password must contain at least
       one uppercase letter
       one lowercase letter
       and one number.
       It must be between 8 and 15 characters long\n""")

#passwordChecks is a list of flags, one flag for each cehck carried out.
#All flags will be set to 1 if all four conditions for a valid password are met
passwordChecks = [0,0,0,0]

#input password
password = input("Please enter new password: ")

while passwordChecks != [1,1,1,1]:
    if len(password)>=8 and len(password)<=15:
        passwordChecks[0] = 1
    for letter in password:
        if letter in lcaseLetters:
            passwordChecks[1] = 1
        if letter in ucaseLetters:
            passwordChecks[2] = 1
        if letter in numbers:
            passwordChecks[3] = 1
    if passwordChecks != [1,1,1,1]:
        password = input("\nInvalid password - please re-enter: ")
        passwordChecks = [0,0,0,0]

print("\nPassword accepted")
input("Press Enter to exit ")
            
