#Program name: Ch 4 Example 7 endless loop.py
print("\nThis program demonstrates how you can get into an endless loop")
print("\nYou can stop it by selecting Shell, Interrupt Execution")
print("from the menu in the Python Shell window.\n")

name = input ("Enter a name, xxx to end: ")
while name != "xxx":
      print("Number of letters in name:",len(name))
