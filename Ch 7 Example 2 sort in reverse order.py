#Program name: Ch 7 Example 2 sort in reverse order.py

alist = [6,2,8,4,0,2,33]
blist = sorted(alist)

print ("Unsorted list: ", alist)
print ("Sorted list: ", blist)

for number in sorted(alist):
    print(number)

print("...and in reverse order:")
blist = sorted(alist, reverse = True)
print (blist)
