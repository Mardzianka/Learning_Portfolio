#Program name: Ch 6 Example 1 try except.py
#Program to demonstrate data validation

print ("This program accepts integers or real numbers\n"+
        "and finds the total and average of the numbers.")
print ("Enter 'end' to signal end of data antry.")        

total = 0
count = 0
number = input("Please enter a number: ")

#convert the number to lowercase so that whatever case
#is used to input "end", it will be recognised

while number.lower() != "end":
    try:
        float(number)
    except ValueError:
        print ("This is not a number")
    else: 
        number = float(number)
        total += number
        count += 1    
    number = input("Please enter next number, 'end' to finish : ")
    
average = total/count
print ("\nTotal =", total, " Average = ", round(average,2))

input ("\nPress Enter to continue ")
