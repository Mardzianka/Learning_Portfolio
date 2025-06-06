#Program name: Ch 5 Example 3 exam results.py
#program prints list of exam results and highest result.

studentNames =["Khan, Afridi    ", "Milner, Angela  ", \
"Philips, Justine", "Osmani, Pias    "]
results = []
topMark = 0
numberOfStudents = len(studentNames)
for student in range(numberOfStudents):
    print("Enter mark for",studentNames[student],": ",end = " ")
    mark = int(input())
    results.append(mark)
    if mark > topMark:
        topMark = mark
        topStudent = studentNames[student]

print("\nStudent\t\t\tExam mark")
for student in range(numberOfStudents):
    print(studentNames[student],"\t",results[student])

print("\nTop result: ",topStudent,topMark)
