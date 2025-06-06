user_inputs = []
while True:
    user_input = input("Please enter a number (enter -1 to EXIT): ")
    
    if user_input.isdigit():
        user_input = int(user_input)
        
        if user_input == 0:
            print("0 is not a valid input.")
            continue
        elif user_input != "0":
            user_inputs.append(user_input)
    elif user_input == "-1":
        if user_inputs:
            average = sum(user_inputs) / len(user_inputs)
            print("The average of user numbers is:", average)
        else:
            print("No valid numbers were entered.")
        break
    else:
        print("That's not a valid input. ")


