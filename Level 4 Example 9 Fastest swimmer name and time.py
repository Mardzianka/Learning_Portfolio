#Program: Level 4 Example 9 fastest swimmer name and time

totalTime = 0
minTime = 100000
moreData = True
while moreData:
    name = input("Enter name of swimmer, xxx to end: ")
    if name != "xxx":
        swimTime = int(input("Enter time in seconds for " + name + ": ")) 
        if swimTime < minTime:
            minTime = swimTime
            fastestSwimmer = name
    else:
        moreData = False

print("Fastest swimmer:", fastestSwimmer)
print("Time:", minTime, "seconds")
