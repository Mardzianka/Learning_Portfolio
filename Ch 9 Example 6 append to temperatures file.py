#Program name: Ch 9 Example 6 append to temperatures file.py
#Program to create or append to a file named temperatures.txt

tempsFile = open("temperatures.txt", "a")
print("This program writes temperature data to \
temperatures.txt")
print("If the file does not exist, it will be created")
city = input("Enter city name, xxx to end: ")

while city != "xxx":
    temperature = input("Enter temperature: ")
    localTime = input("Enter local time: ")
    tempsFile.write(city + "," + temperature + "," + localTime
                    + "," + "\n")
    city = input("Enter city name: ")

#endwhile
tempsFile.close()
