#Ch 6 Question 1 length check.py

prodCode = input("Please enter 6-character product code: ")
while len(prodCode) != 6:    
    print("Invalid code")
    prodCode = input("Please enter 6-character product code: ")
input("Product code accepted - press Enter to exit ")
