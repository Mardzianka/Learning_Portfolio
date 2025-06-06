#Program name: Chapter 4 Example 2 multiplication tables.py
#prints the times tables from 2 to 10

for table in range(2,11):
    print("\n" + str(table) + " Times Table ")
    for n in range(2,13):
        print (str(table) + " x " + str(n)+ " = " + str(table * n))

input("\nPress Enter to continue ")
