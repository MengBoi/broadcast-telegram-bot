import re


def contains_only_digits_and_single_dot(input_str):
    # Define a regular expression pattern that matches only digits and a single dot
    pattern = r'^\d+(\.\d+)?$'

    # Use the re.match() function to check if the input string matches the pattern
    if re.match(pattern, input_str):
        return True
    else:
        return False


print(contains_only_digits_and_single_dot("242343.2."))
