#Program name: Ch15 Example 1 with errors.py
#Validates and counts tickets sold over 4 performances

total = 0

for performance in range(5):
    flag = False
    number = input("Please enter tickets sold for performance "
    + str(performance+1) + ": ")

    while flag == False:
        try:
            int(number)
        except ValueError:
            print ("This is not a valid number")
            flag = False
        else: 
            flag = True
            
        if flag:
            number = int(number)
            if number in range (120):
                total += number
            else:            
                number = input
                ("Please re-enter tickets sold for performance "
                + str(performance+1) + ": ")

average = total/4
print("\nTotal tickets sold: ",total)
print("\nAverage number of tickets per performance ", average)
input("\nPress Enter to exit ")

    
         
