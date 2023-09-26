# Example : Function return value with User Input(My Example)
calculation_to_units = 24


def days_to_units(num_of_days):
    return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"


user_input = input("(My Example)Enter Number of days here:")  # all input take as STRING
my_var = int(user_input)  # Convert string into integer and store into variable
print(days_to_units(my_var))  # Print function with return value

print("\n")


# Example :Function return value with User Input (NANA)
def days_to_units(num_of_days):
    return f"{num_of_days} Days Are {num_of_days * calculation_to_units} Hour"


user_input = input("(NaNa Example)Enter Number of days here: ")  # all input take as STRING
my_var = int(user_input)  # Convert string into integer and store into variable
cal_var = days_to_units(my_var)  # function return value and store in variable
print(cal_var)  # Prin variable
