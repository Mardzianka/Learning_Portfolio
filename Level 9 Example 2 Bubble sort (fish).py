#Program name: Level 9 Example 2 Bubble sort (fish)
fish = ["parrotfish", "grouper", "boxfish", "damselfish",\
        "snapper", "ray"]

#get number of items in the array
numItems = len(fish) 
passNumber = numItems - 1
swapMade = True
while passNumber > 0 and swapMade:
    swapMade = False
    for j in range(passNumber):
        if fish[j] > fish[j + 1]:
            temp = fish[j]
            fish[j] = fish[j + 1]
            fish[j + 1] = temp
            swapMade = True
    passNumber = passNumber - 1
print("\nSorted list:\n",fish)
