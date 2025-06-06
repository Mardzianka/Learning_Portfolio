#Program name: Ch 7 Question 3 sort 2-D list.py
studentMarks = [["Harvey","Ron",56],
                ["Jones","Alan",85],
                ["Lansbury", "Christine", 68],
                ["Mills","David", 72]]
#sort on column 0
studentNamesAscending = sorted(studentMarks, key=lambda x:x[0])

print("Ascending order of surname")
for n in range(len(studentMarks)):
	print (studentNamesAscending[n])
	
input("\nPress Enter to exit ")
