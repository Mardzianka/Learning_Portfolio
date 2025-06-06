#Program name: Ch 2 Exercise 3 rounding floating point numbers.py
#prints the sum and product of two floating point numbers

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
sum = num1 + num2
roundedSum = round(sum,2)
print("The sum of ", num1,"and ",num2, "is", roundedSum)

#Here is a second way of printing the answer to a calculation
#The numbers have been converted to strings so the + sign can be used
#to concatenate the parts of the sentence, and
#the answer has been rounded to three decimal places
product = round(num1 * num2,3)
print("The product of " + str(num1) + " and " + str(num2) + " is " + str(product))     
