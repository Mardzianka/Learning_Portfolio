#Program name: Ch 7 Exercise 1.py
#program holds a dictionary of anagrams
#User can type in a word and the program returns a list of anagrams
anagrams = {"angel": ("angle","glean"),
            "trade":("rated","tread"),
            "predator": ("parroted","teardrop"), 
            "garden": ("danger","gander","ranged"),
            "berate": ("beater", "rebate")}

word = input ("Enter word for which you would like to see anagrams: ")            
while word != "end":    
    if word in anagrams:
        print(anagrams[word])
    else:
        print("Word not found\n")
    word = input ("Enter another word - enter 'end' to quit: ")

input ("\nPress Enter to exit program: ")
