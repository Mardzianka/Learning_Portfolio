#Program name: Ch 3 Exercise 4 discount on goods purchased.py 
#calculates discount depending on value of goods purchased

goodsValue = float(input("Enter value of goods purchased: "))

if goodsValue >= 200:
    discount = 0.1*goodsValue
elif goodsValue >= 100:
    discount = 0.05*goodsValue
else:
    discount = 0

amountOwed = goodsValue - discount
print("Value of goods:",goodsValue," Discount:",discount, \
      " Amount owing:",amountOwed)
    
