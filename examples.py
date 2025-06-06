#true or false
#True False
my_bool = True

print(type(my_bool))
is_raining = False
logged_in = True

#conditional statement:
is_smaller = (10 < 15)
is_larger = (20 > 7)
is_equal = (10 == 10)

#print(is_smaller)
#print(is_larger)
#print(is_equal)

is_smaller = (20 <= 15)
is_larger = (20 >= 7)
is_equal = ('Hello' == 'hello')

print(is_smaller)
print(is_larger)
print(is_equal)

#conditions


if True:
    print("If this prints the condition is True!")

    #if true will print
    #if false wont print

is_raining = True
#If et as true above it will print, if above set as false it wont print
if is_raining:
    print("It is raining outside! ") 

    #if indented itv refers to if (same level) as if,
    #  when moved back its a separate code,
    #  not condition for if

#again because raining is set as true it wont print if false

rain_volume = 3
if rain_volume > 2:
    is_raining = True

if is_raining:
    print("It is raining outside! ")

#if its not raining else

if is_raining:
    print("Is raining outside! ")
else:
    print("Its not raining outside! ")


    #elif else if

num1 = 5
num2 = 10

if num1 == num2:
    print("The numbers are equal.")
elif num1 > num2:
    print(f"{num1} is larger than {num2}")
else:
    print(f"{num2} is larger than {num1}")




#create a programe that will ask a user to provide their last 3 test scores
# and determine their grade and determine their grade avarage
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 50-59 E
# < 50 F


score1 = input("please enter the 1st score: ")
score2 = input("please enter the 2st score: ")
score3 = input("please enter the 3st score: ")

score1 = int(score1)
score2 = int(score2)
score3 = int(score3)

total = score1 + score2 + score3
avarage = total/3


if avarage >= 90:
    print("Grade Score: A")
elif avarage >= 80:
    print("Grade Score: B")
elif avarage >= 70:
    print ("Grade Score: C")
elif avarage >= 60:
    print("Grade Score: D")
elif avarage >= 50:
    print("Grade Score: E ")
else:
    print("FAILED ")







