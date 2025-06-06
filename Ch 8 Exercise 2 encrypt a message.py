#Program name: Ch 8 Exercise 2 encrypt a message.py
"""
Calls a function to encrypt the message by rearranging the letters
in the sequence 2,4,6,...1,3,5...
For example, "Hello Jo" will be encrypted as el oHloJ.
"""

def encrypt(message):
    jumbledMessage = ""
    
    chars = len(message)
    for n in range (1,chars,2):
        letter = message[n]
        jumbledMessage += letter
    
    for n in range(0,chars,2):
        letter = message[n]
        jumbledMessage += letter
    return(jumbledMessage)
    
#main program
message = input("Enter your message: ")
encryptedMessage = encrypt(message)
print(encryptedMessage)
input("Press Enter to exit ")
