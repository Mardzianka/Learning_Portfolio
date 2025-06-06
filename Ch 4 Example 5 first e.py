#Program name: Ch 4 Example 3 first e.py
#Find first occurrence of the character e in a sentence
#If there is no character e, print an appropriate message
eIndex = -1
sentence = input ("Please enter a sentence: ")
for ePosition in range(len(sentence)):
    if sentence[ePosition] == "e":
        eIndex = ePosition
        print ("Index of first 'e' is ", eIndex)
        break

if eIndex == -1:
    print ("There is no 'e' in the sentence.")
   
input("\nPress Enter to exit ")
