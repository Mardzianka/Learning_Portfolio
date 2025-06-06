"""
Program name: Ch 5 Exercise 5 top game score.py
Program accepts user ID, and checks if it is in the list of players
If not, it is appended to the list, with a score of 0.
User plays the game and is assigned a random score between 50 and 200
Program checks if it is greater than the score held.
If so, it replaces it.
The user ID and score is then printed out.
"""
import random
scores = [["AAA01",135],
          ["BBB01",87],
          ["CCC01",188],
          ["DDD01",109]
          ]
userID = ""
userID = input ("Please enter userID: ")

# check whether user ID is in list
while userID !="xxx":    
#    print ("len (scores) = ",len(scores))
    listLength = len(scores)
    found = False
    for n in range (listLength):
        if userID in scores[n][0]:
            print ("Found at position ",n)
            found = True
            position = n
    if not found:
        print("UserID not found... appending it at position ", listLength)
        position = listLength
        scores.append([userID,0])
    print(scores)
          
    #generate a random score          
    gameScore = random.randint(50,200)
    print("\nScore for this game: ",gameScore)
    if gameScore > scores[position][1]:
        scores[position][1] = gameScore
    print (scores)          
    #play again with the same or a different user
    userID = input ("Please enter userID, xxx to end: ")
input("Press Enter to exit ")
