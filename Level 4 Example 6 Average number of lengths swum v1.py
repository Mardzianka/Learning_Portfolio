#Program name: Level 4 Example 6 Average number of lengths swum v1

day = 0
totalLengths = 0
lengths = int(input("Enter number of lengths: "))
while lengths != -1:
    day = day + 1
    totalLengths = totalLengths + lengths
    lengths = int(input("Enter number of lengths, -1 to end: "))

averageLengths = totalLengths / day
print("Average daily number of lengths:", averageLengths)


    
