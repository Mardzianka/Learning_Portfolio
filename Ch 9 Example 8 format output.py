#Program name: Ch 9 Example 8 format output.py
#Reads the file temperatures.txt, converts centigrade to farenheit.
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
    localTime = cityRec[2]
    
    newCityRec.append(city)
    newCityRec.append(temperatureC)
    newCityRec.append(tempF)  
    newCityRec.append(localTime)
    cityTable.append(newCityRec) 
    #clear the row in the new table ready to append the next row from the text file   
    newCityRec = []
    
#All the records are now held in a two-dimensional list called cityTable
#The list needs to be sorted in descending sequence on temperatureC
#Refer to Chapter 7 for how to do this using the lambda function
#Print the data 
sortedTable = sorted(cityTable, key = lambda x: x[1], reverse = True)

print("List of cities in descending order of temperature\n")
#print column headings
print("%-20s%20s%20s%20s"
%("City","Temperature(C)","Temperature(F)","Local time"))
for n in range (len(sortedTable)):
    print ("%-20s%20.1f%20.1f%20s" 
           %(sortedTable[n][0],sortedTable[n][1],sortedTable[n][2],
             sortedTable[n][3]))
tempsFile.close()

input ("\nPress Enter to exit ")
