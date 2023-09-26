# Example 2: (ONE Function) Whole calculation in program
from operator import ifloordiv

print("main:program Run")

calculation_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"


def validate_and_execute():  # write like Nana
    try:
        user_number = int(num_of_days_element)  # for loop variable given into integer and store into variable
        if user_number > 0:
            print(days_to_units(user_number))
        elif user_number == 0:
            return "you have enter 0 so enter any positive value"
        else:
            return "You Have enter negative Value"

    except ValueError:
        print("Your input is invalid or text , Please enter valid number")


user_input = ""
while user_input != "exit":
    user_input = input("Enter Number of days here:")  # all input take as STRING
    for num_of_days_element in user_input:
        validate_and_execute()  # function call for check input string or number

