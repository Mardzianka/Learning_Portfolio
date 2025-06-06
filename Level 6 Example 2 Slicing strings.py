#Program name: Level 6 Example 2 Slicing strings
#This program shows how to isolate parts of a string

productCode = "TV44-BHD"

#isolate first 4 characters
chars1to4 = productCode [0:4]
print("First four characters are " + chars1to4)

#Find length of product code
n = len(productCode)
print("Length of product code:" , n)

#isolate last 3 characters
last3chars = productCode[n-3:n]
print("Last three characters are:", last3chars)

