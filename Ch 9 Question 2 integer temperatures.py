#Program name: Ch 9 Question 2 integer temperatures.py
#This version produces fomatted output
#Reads the file temperatures.txt, converts centigrade to farenheit.
#Fahrenheit temperature is converted to Integer
#Appends all the fields including the new field, to a list called newCityRec
#The list newCityRec is then appended to cityList to form a two-dimensional list
#cityList is then sorted on descending order of temperature
#and report with both centigrade and farenheit temperatures is printed

tempsFile = open("temperatures.txt", "r")

cityTable = []
newCityRec = []

for row in tempsFile:
    cityRec = row.split(",")
    
    city = cityRec[0]
    temperatureC = float(cityRec[1])
    tempF = (temperatureC * 9/5) + 32
    tempF = int(tempF)
    temperatureC = int(temperatureC)
    localTime = cityRec[2]
    
    newCityRec.append(city)
    newCityRec.append(temperatureC)
    newCityRec.append(tempF)  
    newCityRec.append(localTime)
    cityTable.append(newCityRec) 
    print(newCityRec) #just to see what's going on
   
    newCityRec = []
    
#All the records are now held in a two-dimensional list called cityTable
#The list needs to be sorted in descending sequence on temperatureC
#Refer to Chapter 7 for how to do this using the lambda function

sortedTable = sorted(cityTable, key = lambda x: x[1], reverse = True)

print("\nList of cities in descending order of temperature\n")
for n in range (len(sortedTable)):
    print (sortedTable[n][0],sortedTable[n][1],
           sortedTable[n][2],sortedTable[n][3])
