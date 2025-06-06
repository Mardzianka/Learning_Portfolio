#Program name Ch 5 Exercise 1 list operations.py

alist = []
alist.append("apple")
print("alist =",alist)

blist = [0] *20
print("blist =",blist)

clist = alist + blist
print("clist 2",clist)

lastC = clist.pop()
print("lastC",lastC)
