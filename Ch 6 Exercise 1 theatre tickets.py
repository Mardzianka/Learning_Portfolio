#Program name: Ch6 Exercise 1 theatre tickets.py
#Validates and counts tickets sold by Dramatic Society

total = 0

for performance in range(4):
    flag = False
    number = input("Please enter tickets sold for performance "\
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
            if number in range (121):
                total += number
            else:
                flag = False
                print("Must be in the range 0 to 120")
                number = input("Please re-enter tickets sold for performance "\
                + str(performance+1) + ": ")
        else:
            number = input("Please re-enter tickets sold for performance "\
            + str(performance+1) + ": ")
average = total/4
print("\nTotal tickets sold: ",total)
print("\nAverage number of tickets per performance ", average)
input("\nPress Enter to exit ")

    
         
