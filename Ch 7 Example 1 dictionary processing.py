#Program name: Ch 7 Example 1 dictionary processing.py

studentMarks = {"Wesley":5,"Jo":9,"Betty":6, "Robina":5}
#Example 1a: Looking up a value
name = input ("Enter a student name to look up: ")
if name in studentMarks:
    print("Mark: ", studentMarks[name])
else:
    print("Name not found")

#Example 1b: Adding a new key-value pair
#Before adding a new key-value pair,
#you should check that the key is not already in the dictionary:
name = input ("Enter a student name to add: ")
if name in studentMarks:
    print("Name is already in the marks record")
else:
    mark = int(input("Enter mark: "))
    studentMarks[name] = mark
print(studentMarks)

#Example 1c: Editing a value in an existing key:value pair
name = input ("Enter a student name to edit their mark: ")
if name in studentMarks:
    mark = int(input("Enter mark: "))
    studentMarks[name] = mark
else:
    print("Name not found")

#Example 1d: Deleting a key:value pair
name = input ("Enter a student name to delete: ")
if name in studentMarks:
    del studentMarks[name]	
else:
    print("Name not found")
print(studentMarks)

#Example 1e: Sorting a dictionary in order of keys
studentSorted = sorted(studentMarks.keys())
print ("\nSorted names")
for name in sorted(studentMarks.keys()):
    print (name, studentMarks[name]) 
