#Program name: Level 10 Example 6 Print renewables file formatted in columns
#Reads records from a text file named renewables2019.txt
#and prints country names and percentage renewable energy generated

energyFile = open("renewables2019.txt","r")
endOfFile = False
#print headings
print("Country      Wind    Solar   Hydro   % renewables")
while not endOfFile:
    energyRec = energyFile.readline()
    if energyRec =="":
        endOfFile = True
    else:
        #split the record into individual fields 
        #comma is the field separator
        fieldList = energyRec.split(",") #comma is the field separator
        country = fieldList[0]
        wind = float(fieldList[1])
        solar = float(fieldList[2])
        hydro = float(fieldList[3])        
        percentRenewables = float(fieldList[4])

#The format() method allows you to print in neat columns        
        print("{:10}{:8.2f}{:8.2f}{:8.2f}{:8.1f}"\
              .format(country,wind,solar,hydro,percentRenewables))
        

# This is another way of writing the format statement:       
#        
#        print("{:10}".format(country) + "{:8.2f}".format(wind)+ \
#"{:8.2f}".format(solar) + "{:8.2f}".format(hydro) \
#+ "{:8.2f}".format(percentRenewables))
        
        
        
