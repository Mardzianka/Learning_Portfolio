#create simple calculator#
#requirments
# the user can
#1.select an operation(add, sub,multiply,divide)
#2. input 2 numbers
#3. get result from operation
# 4. exit the applikation
#. program should handle invalid input

#STEP 3 DESIGN 
##      define functions
#           add(num1, num2)
#           subtract (num1, num2)
#           multiply()
#           divide(num1, num2)
# IMPLEMENT A MENU
# ADD
# SUBTRACT
# MULTIPLY
# DIVIDE
# exit

# STEP4 IMPLEMENTATION

MENU = """Basic Calculator Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
0. Exit"""


while True:
    print(MENU)
    
    choice = input(": ")
    if choice in {"1", "2"}, {"3"}, {"4"}:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    if choice == "1":
        result = num1 + num2

    elif choice == "2":
        result = num1 - num2
        
    elif choice == "3":
        result = num1 * num2
        
    elif choice == "4":
        result = num1 / num2

        print("-"*40)
        print(f"The result is:  {result}")

else



        