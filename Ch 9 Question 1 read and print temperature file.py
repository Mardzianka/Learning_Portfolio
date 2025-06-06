#Program name: Ch 9 Question 1 Read and print temperature file.py
#Reads the file temperatures.txt, and prints all the records in the file

tempsFile = open("temperatures.txt", "r")

for row in tempsFile:
    cityRec = row.split(",")    
    city = cityRec[0]
    temperatureC = cityRec[1]    
    localTime = cityRec[2]
    print(city, temperatureC, localTime)
tempsFile.close()
    
