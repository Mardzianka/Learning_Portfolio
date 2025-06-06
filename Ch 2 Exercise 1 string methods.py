#Program name: Ch 2 Exercise 1 string methods.py
#demonstrates string methods and functions

proverb = "A picture's worth a thousand words"
proverbImage = proverb.replace("A picture's","An image is")
print("amended proverb ",proverbImage)

firstO = proverb.find("o")
print("First occurrence of 'o' is at index",firstO)

proverbUpper = proverb.upper()
print("Uppercase string :",proverbUpper)

print("Length of string =",len(proverb))

