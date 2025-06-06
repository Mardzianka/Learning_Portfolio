swimming = input('Please provide your swimming time in minutes: ')
cycling = input('Please provide your cycling time in minutes: ')
running = input('Please provide your running time in minutes: ')
num1 = int(swimming)
num2 = int(cycling)
num3 = int(running)
total = num1 + num2 +num3
print("Triathlon total time: ", total)

if total <= 100:
    print('Honorary colours  ')
elif total >= 101 and total <= 105:
    print('Honorary half colours ')
elif total >= 106 and total <= 110:
    print('Honorary scroll ')
else:
    print('No award')












