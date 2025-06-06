#Program name: Level 4 Example 8 Average number of lengths swum v2

day = 0
totalLengths = 0
moreData = True
print("Enter -1 when no more data")
while moreData:
    lengths = int(input("Enter number of lengths on day " + str(day+1)+": "))
    if lengths != -1:
        day = day + 1
        totalLengths = totalLengths + lengths
    else:
        moreData = False
averageLengths = totalLengths/day
print("Average daily number of lengths:", round(averageLengths,1))

    
