#Program name: Ch 7 Example 1 sort 2-D list.py
studentMarks = [	["Harvey","Ron",56],
	["Jones","Alan",85],
	["Lansbury", "Christine", 68],
	["Mills","David", 72] ]
#sort on column 2
studentMarksAscending = sorted(studentMarks, key=lambda x:x[2])
studentMarksDescending = sorted(studentMarks,
                                key=lambda x:x[2], reverse = True)
print("Ascending order of mark")
for n in range(len(studentMarks)):
	print (studentMarksAscending[n])
print("\nDescending order of mark")    
for n in range(len(studentMarks)):
	print(studentMarksDescending[n])
	
input("\nPress Enter to exit ")
