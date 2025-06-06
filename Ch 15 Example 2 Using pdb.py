#Program name: Ch 15 Example 2 Using pdb.py
import pdb
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
pdb.set_trace()
if x == y:
    z = x*x
elif x > y:
    z = x - y
else:
    z = x + y
print("x =",x," y =",y, " z =",z)
