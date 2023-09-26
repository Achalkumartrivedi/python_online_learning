# Example : Validate User input with IF/Else
print("START VALIDATE USER INPUT PROGRAM")
print("First Program: positive return calculation ,negative return message")
# Program : if input is greater than 0 than return calculation or enter negative value than print message only
calculation_to_units = 24


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"
    else:
        return "You Have Entered NEGATIVE Value"


user_input = input("Enter Number of days here:")  # all input take as STRING
my_var = int(user_input)  # Convert string into integer and store into variable
print(days_to_units(my_var))  # Print function with return value

print("\n")
print("Second Program: check if number is positive than TRUE other is FALSE")
# Program : same program with TRUE AND FALSE check
calculation_to_units = 24


def days_to_units(num_of_days):
    check_boolean = num_of_days > 0  # check boolean data type and store into variable
    print(f"Positive value: {check_boolean}")
    if num_of_days > 0:
        return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"
    elif num_of_days == 0:
        return "you have enter 0 so enter any positive value"
    else:
        return "You Have enter negative Value"


user_input = input("Enter Number of days here:")  # all input take as STRING
my_var = int(user_input)  # Convert string into integer and store into variable
print(days_to_units(my_var))  # Print function with return value

print("\n")
print("Third Program: Check User input integer or string ,check number positive,zero and negative")
# Program : same program - Check user input as integer or string ,check positive other 0 and negative show message
calculation_to_units = 24


def days_to_units(num_of_days):
    check_boolean = num_of_days > 0  # check boolean data type and store into variable
    print(f"Positive value: {check_boolean}")
    if num_of_days > 0:
        return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"
    elif num_of_days == 0:
        return "you have enter 0 so enter any positive value"
    else:
        return "You Have enter negative Value"


user_input = input("Enter Number of days here:")  # all input take as STRING

if user_input.isdigit():  # this function not allow flot ,negative,text value
    my_var = int(user_input)  # Convert string into integer and store into variable
    print(days_to_units(my_var))  # Print function with return value
else:
    print("Your input is not valid number , Please enter valid number")
