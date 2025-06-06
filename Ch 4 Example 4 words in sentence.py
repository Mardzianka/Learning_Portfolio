#Program name: Ch 4 Example 3 words in sentence
#count the number of words in a piece of text input by the user.
sentence = input ("Enter a sentence: ")
numWords = 1
for letter in sentence:
    if letter == " ":
        numWords += 1
print ("Number of words =",numWords)
print ("Number of characters = ", len(sentence))

input ("\nPress Enter to exit ")
