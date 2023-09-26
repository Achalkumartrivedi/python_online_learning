calculation_to_units = 24
name_of_unit = "Hour"


# Example : Function return value
def days_to_units(num_of_days):
    return f"{num_of_days} Days Are {num_of_days * calculation_to_units} {name_of_unit}"


my_val = days_to_units(1)
print(my_val)
my_val2 = days_to_units(2)
print(my_val2)
my_val3 = days_to_units(3)
print(my_val3)

#if we have value as function execution that we have to return value using "return" keyword