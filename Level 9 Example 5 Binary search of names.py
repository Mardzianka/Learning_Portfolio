#Program name: Level 9 Example 5 Binary search of names
#The list to be searched contains 12 names
aList = ["Ava", "Danesh", "Fred", "George", "Ishaan", "Jas", \
         "Ken", "Lila", "Manesh", "Oliver", "Peter", "Tabu"]

print("List of names to be searched:",aList)
found = False
first = 0
last = len(aList) - 1
searchItem = input("Enter name you are looking for: ")

while not found and first <= last:
    midpoint = int((first + last)/2)
    if aList[midpoint] == searchItem:
        found = True
        index = midpoint        
    else:
        if aList[midpoint] < searchItem:
            first = midpoint + 1
        else:
            last = midpoint - 1
#endwhile
if found:
    print("Found at position",index,"in the list, starting at 0")
else:
    print("Item is not in the list")

