# def new_function():
#     print('Hello')
#     print('world!')

#     # parameters
#     def new_function(text):
#         print(text)

#     new_function('Hello')
#     new_function('Goodbye')

#     my_text = 'This is my text'
#     my_function = my_text

def draw_line():
    print('-' *80)

# draw_line()
# print("This is sentence!")
# draw_line()

def draw_line(symbol, lenght):
    print(symbol*lenght)

draw_line('_', 80)
draw_line("-", 40)
draw_line("#", 55)

# returning

def get_average(num1, num2, num3):
    avarage = (num1+num2+num3)/3
    return avarage
result = get_average(5, 8, 12)
result += 10
print(result)

def draw_line(symbol, lenght):
    return (symbol*lenght) + "\n"
my_str = draw_line("-", 10) + ("MAIN MENU\n") + draw_line("-", 10)











