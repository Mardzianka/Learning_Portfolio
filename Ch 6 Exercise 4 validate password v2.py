#Prgram name Ch 6 Exercise 4 validate password v2.py
#Alternative version
'''
Password validation program
Password must be between 8 and 15 characters and contain
at least one uppercase, one lowercase and one numeric character
'''
print("Password must be between 8 and 15 characters")
print("and contain at least one lowercase letter,")
print("one uppercase letter and one number.\n")
password = input("Please enter new password: ")
passwordValid = False
uppercasePresent = False
lowercasePresent = False
numberPresent = False
validLength = False
while not passwordValid:
    if (len(password)>=8) and (len(password)<=15):    
            validLength = True
            
    for n in range(0,len(password)):
# this is one way of checking for a number...
#       if password[n] in ("0","1","2","3","4","5","6","7","8","9"):
#or use the ord function to convert the character to its ASCII value
        if ord(password[n]) in range (48,58):
            numberPresent = True

# You could use the ord function here too, range (65,91),
#instead of the statement below
# Note the backslashes indicating a multi-line statement
        if password[n] in ["A","B","C","D","E","F","G","H","I","J","K",\
                           "L","M","N","O","P","Q","R","S","T","U",\
                           "V","W","X","Y","Z"]:
            uppercasePresent = True
                   
        if password[n]in ["a","b","c","d","e","f","g","h","i","j","k",\
                          "l","m","n","o","p","q","r","s","t","u",\
                          "v","w","x","y","z"]:
            lowercasePresent = True 
            
    if (uppercasePresent == True) \
       and (lowercasePresent == True) \
       and (numberPresent == True) \
       and validLength == True:
        passwordValid = True
    else:
        uppercasePresent=lowercasePresent=numberPresent=validLength=False        
        password = input("Invalid password - please re-enter: ")
        

print ("Password accepted")
input("\nPress Enter to exit")
