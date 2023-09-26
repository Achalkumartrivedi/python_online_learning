# Topic - CLean Up Code (Make useful function)

# Example 1: (Two Function)Make another function to Check user input as integer or string
# other function is check number zero ,greater or negative
print("Example 1: Calculation with one function")
calculation_to_units = 24


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"
    elif num_of_days == 0:
        return "you have enter 0 so enter any positive value"
    else:
        return "You Have enter negative Value"


def validate_and_execute():  # write like Nana
    if user_input.isdigit():  # this function only allow digit, not allow flot ,negative,text value
        user_number = int(user_input)  # convert user input into integer and store into variable
        converted_input_value = days_to_units(user_number)  # function call and store into variable
        print(converted_input_value)
    else:
        print("Your input is invalid or text , Please enter valid number")


user_input = input("Enter Number of days here:")  # all input take as STRING
validate_and_execute()  # function call for check input string or number

print("\n")
# Example 2: (ONE Function) Whole calculation in program

print("Example 2: More Cleanup - calculation in one function only")

calculation_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"


def validate_and_execute():  # calculation in one function
    if user_input.isdigit():  # this function only allow digit, not allow flot ,negative,text value
        user_number = int(user_input)  # input into integer and store into variable
        if user_number > 0:
            converted_input_value = days_to_units(user_number)  # function call and store into variable
            print(converted_input_value)
        elif user_number == 0:
            return "you have enter 0 so enter any positive value"
        else:
            return "You Have enter negative Value"

    else:
        print("Your input is invalid or text , Please enter valid number")


user_input = input("Enter Number of days here:")  # all input take as STRING
validate_and_execute()  # function call for check input string or number
