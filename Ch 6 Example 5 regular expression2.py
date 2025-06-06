#Program name: Ch6 Example 5 regular expression2.py
#program uses a regular expression to check for valid product code

import re   #imports regular expression module
print ("A valid product code starts with one or two \
uppercase letters,\nfollowed by four or more digits,\n\
and ends with either H or G\n")

productCode = input ("Enter a product code ('x' to end): ")
while productCode != "x":
    valid = re.match("[A-Z]{1,2}[0-9]{4,}[HG]", productCode)
    if valid:
        print ("Valid product code entered")
    else:
        print ("Invalid product code")
    productCode = input ("Enter a product code ('x' to end): ")
input("\nPress Enter to exit ")
    
