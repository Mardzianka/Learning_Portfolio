#Program name: Ch 4 Exercise 3 product codes.py

totalAB = 0
total00 = 0
productCode = input("Enter 5-character product code, xx to end: ")
first2chars = productCode[0:2]

while first2chars != "xx":
    last2chars = productCode[3:5]
    if first2chars == "AB" or first2chars =="AS":
        totalAB += 1
    if last2chars == "00":
        total00 += 1
    productCode = input("Enter 5-character product code, xx to end: ")
    first2chars = productCode[0:2]
        
print("Total codes starting with 'AB' or 'AS' = ",totalAB)
print("Total codes ending '00': ", total00)

input("\nPress Enter to exit ")
