#Program name: Level 4 Examples 1-4 different ranges in FOR loops

#Example 1
print("\nExample 1: print 7 times table from 2 to 10")
for count in range(2,11):
    n = count * 7
    print(count, "x 7 =",n)

#Example 2
print("\nExample 2: print numbers and their squares from 0 to 4")
for j in range(5):
    jsquared = j*j
    print (j, jsquared) 

#Example 3
print("\nExample 3: print every 7th number between 0 and 35")
for n in range(0,36,7):
    print(n)

#Example 4
print("\nExample 4: print every 7th number between 35 and 7 in descending order")
for n in range(35,6,-7):
    print(n)

