# Example : TRY/EXCEPT Program (try/catch in another langauge)
# SYNTAX : try: / except ValueError:

print("Example : calculation in one function with TRY:/EXCEPT ValueError:")

calculation_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"


def validate_and_execute():  # calculation in one function with TRY/EXCEPT
    try:
        user_number = int(user_input)  # input into integer and store into variable
        if user_number > 0:
            converted_input_value = days_to_units(user_number)  # function call and store into variable
            print(converted_input_value)
        elif user_number == 0:
            return "you have enter 0 so enter any positive value"
        else:
            return "You Have enter negative Value"

    except ValueError:
        print("Your input is invalid or text , Please enter valid number")


user_input = input("Enter Number of days here:")  # all input take as STRING
validate_and_execute()  # function call for check input string or number
