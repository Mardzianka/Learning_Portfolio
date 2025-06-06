#Program name: Ch 3 Example 1 assigning student grades
#program assigns a grade of A, B, C or F depending on mark entered by user

mark = int(input("Enter mark: "))
if mark >=75:
    grade = "A"
elif mark >=60:
    grade = "B"
elif mark >=50:
    grade = "C"
else:
    grade = "F"
print("Grade is",grade)
