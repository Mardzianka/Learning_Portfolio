#Program name: Ch 6 Length check.py
prodCode = ""
while len(prodCode) != 6:
    prodCode = input("Please enter 6-character product code: ")
    if len(prodCode) != 6:
        print("Invalid code")
