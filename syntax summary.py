#Program name: Syntax summary
#PG Online Ltd (c) 2021

def inputAndOutput():
    print ('''
Input statement
    name = input("Enter name: ")
    visitors = int(input("How many visitors? "))
    cost = float(input("Enter cost per person: ")) 
    totalCost = visitors * cost

Output statement
    print("Total cost:",totalCost)

    or use concatenation to join two strings:
    print("TotalCost " + str(totalCost))
    
    "end" parameter used here to prevent automatic newline
    print("Total cost ",end="")
    print(totalCost)

   newline character \ followed by n in quotes causes a skip to a new line
''')
    input("Press Enter to continue ")
    
def arithmeticOperators():
    print('''\nArithmetic operators                            Result
    addition                a = 15 + 2           a = 17  
    subtraction             b = 15 - 2           b = 13  
    multiplication          c = 15 * 2           c = 30
    division                d = 15 / 2           d = 7.5
    exponentiation          e = 5**2             e = 25
    integer division (div)  f = 15 // 2          f = 7 
    remainder (mod/modulus) g = 15 % 2           g = 1
    ''')
   
    input("Press Enter to continue ")
    
def relationalOperators():


    print('''   

Logical and Bolean operators
                                                    Examples (a = 3, b = 5)
    less than               <     a < b              True  
    greater than            >     a > b              False
    less than or equal      <=    a <= b             True
    greater than or equal   >=    a >= b             False 
    equal                   ==    a == b             False
    not equal               !=    a != b             True   
    logical and             and   a == b and b == 5  False
    logical or              or    a == b or b == 5   True
    logical not             not   not(a == b)        True
    ''')
    input("Press Enter to continue ")

def selection():
#Selection
    print('''
Selection examples
if statement
    if (age < 17):
        print("you are too young to drive")

if...else statement
    if (score >= 50):
        print("Well done - you have passed ")
    else:
        print("Bad luck, you have failed")

if...elif...else statement
    if (score >= 80):
        print("Well done - you have passed with flying colours")
        print("Distinction")
    elif (score >= 70):
        print("Merit")
    elif (score >= 50):
        print("Pass")        
    else:
        print("Fail")
    
    
 Nested if statement
    if (month == "July" or month == "August"):
        if customer == "Gold":
            weeklyRate = 100
        else:
            weeklyRate = 120
    else:
            weeklyRate = 75
    ''') 
    input("Press Enter to continue ")
   

def forNext():

    print('''
Iteration examples using the for...next loop
    
print numbers 0 to 5:
    for n in range(6):
        print(n)

print numbers 5 to 8:
    for n in range(5,9):
        print(n)

print every third number between 1 and 10 starting at 1:
    for n in range(1,11,3):
        print(n)

print every third number counting down from 99 to 90, counting down
    for n in range(99,89,-3):
        print(n)
    ''')
    input("Press Enter to continue ")


def whileLoop():
    print('''
Indefinite iteration example
while...endwhile loop

    daysRemaining = 6
    while daysRemaining > 0:
        daysRemaining = daysRemaining - 1
        print("Days to Christmas", daysRemaining)
    print("Happy Christmas!")

This prints:
Days to Christmas 5
Days to Christmas 4
Days to Christmas 3
Days to Christmas 2
Days to Christmas 1
Days to Christmas 0
Happy Christmas!
        ''')

    input("Press Enter to continue ")


def lists():
    print('''
Lists
    myList = ["Bob","Mandy","Fred","Jo","Keira"]
    print(myList[0])              prints Bob
    print(myList)                 prints the whole list
    print(len(myList))            prints 5 (the number of items in the list)

    aList = []*100                initialises an empty list of 100 items

Two-dimensional lists
    Example:
    Quiz results for 3 teams and 4 rounds are recorded 
    in a 2-D list with 3 rows and 4 columns
    Row indices go from 0 to 2 (teams)
    Column indices go from 0 to 3 (rounds)

    quizResults =  [[ 5, 7, 9, 4],  (row 0)
                    [12,14,10,18],  (row 1)
                    [27,21,23,20]]  (row 2)

    quizResults[0][0] contains 5, the result for Team 1, Round 1.
    print(quizResults[1][3]) prints 18, the result in second row
                                        and fourth column 

    ''')

    input("Press Enter to continue ")
      
def strings():
    print('''    
Strings
    A string is a sequence of characters enclosed in single or double quotes
    myString = "This is a string"
    len(mystring) evaluates to 16, the number of characters in the string

Iterating through a string
    for nchar in myString:
        print(nchar)

Two useful string methods
    myStringUCase = myString.upper()
    myStringLCase = myString.lower()

Slicing strings
    e.g. to isolate characters 6 to 9 ("is a") of myString:
    chars6to9 = myString[5:8]

    ''')
    input("Press Enter to continue ")

    
def subroutines():
    print(''' 
Subroutines
    There are two types of subroutine: function and procedure
    A function returns a value
    a procedure does not return a value    

Functions
    def myFunction():

    the function may receive parameters:
    def myFunction(a,b):
        x = a + b
        return(x)

    To call the function:
    sum = myFunction(3,4)

Procedures are similar 
    def myproc():

The procedure may receive parameters:
    
    def greet(greeting,name):
        print(greeting, name)

    To call the procedure:
    greet("Hello","Jane")
    
    ''')

    input("Press Enter to continue ")

def libraryModules():
    print(''' 
Generating a random number
Import the random module 
    import random

    n = random.randint(a, b) returns a random integer n where a<=n<=b
    x = random.random()      returns a random float number where 0.0<=x<=1.0 
    
Suspend program execution
Import the time module
    import time

    time.sleep(sec)         suspends execution for sec seconds


Using the turtle
Import the turtle module
    import turtle

Turtle methods
    turtle.forward(100)    moves the given distance in the current direction
    turtle.right(x)        turns through x degrees clockwise, e.g. 90 for right angle
    turtle.penup()         lifts the pen
    turtle.pendown()       puts the pen down
    turtle.pensize(10)     sets the pen size
    turtle.pencolor("red") sets the pen colour
    turtle.setpos(-300,0)  set the coordinates of the turtle
    ''')
    input("Press Enter to continue ")

    
def textFiles():
    print('''
Opening a text file
    A text file must be opened for reading, writing or appending data
    
    gameFile = open("gamescore.txt","r")   to open the file for reading
    gameFile = open("gamescore.txt","w")   to write a new file or overwrite
                                           an existing one
    gameFile = open("gamescore.txt","a")   to append data or create a new file
                                           if no file can be found

Closing a text file
     gameFile.close()
    
Reading a text file
    gameFile.read()           reads the whole file

    gameRec = gameFile.readline()       reads one line of a text file
    This returns an empty string "" on reaching the end of file

Writing or appending a line to a text file
    gameFile.write(field1 + field2 +... +.. )
    (add newline character (escape sequence) \ followed by n as last field)

    ''')
    input("Press Enter to continue ")    

          
#***************************************
#main program
#***************************************

print("This program shows a syntax summary for your chosen topic") 
choice = 0
while choice != 12:
    print('''
1.  Input and output statements
2.  Arithmetic operators
3.  Logical and Boolean operators
4.  Selection statements
5.  Definite iteration (for loops)
6.  Indefinite iteration (while loops)
7.  Lists
8.  Strings
9.  Subroutines
10. Python library modules (random, time, turtle)
11. Text files
12. Quit
    ''')
    choice = input("Select a topic: ")
    #validate choice
    while not choice in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
        choice = input("Please enter a number between 1 and 12: ")

    choice = int(choice)                   
    if choice == 1:
        inputAndOutput()
    elif choice == 2:
        arithmeticOperators()
    elif choice == 3:
        relationalOperators()
    elif choice == 4:
        selection()
    elif choice == 5:
        forNext()
    elif choice == 6:
        whileLoop()
    elif choice == 7:
        lists()
    elif choice == 8:
        strings()
    elif choice == 9:
        subroutines()
    elif choice == 10:
        libraryModules()
    elif choice == 11:
        textFiles()
     
               
