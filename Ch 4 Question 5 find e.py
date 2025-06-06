#Program name: Ch 4 Question 5 find e.py
#Find first occurrence of a given string in a sentence
#If there is no character e, print an appropriate message

sentence = input ("Please enter a sentence: ")
eIndex = sentence.find("e")

if eIndex != -1:
    print("Index of first 'e' is ",eIndex)
else:
    print ("There is no 'e' in the sentence.")
   
input("\nPress Enter to exit ")
