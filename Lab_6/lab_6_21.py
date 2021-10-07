def integer_to_reverse_binary(integer_value):
    """Converts an integer to a string of binary. However, digits are reversed."""
    reverse_binary_string = ''
    while integer_value > 0:
        binary_digit = integer_value % 2
        reverse_binary_string += str(binary_digit)
        integer_value //= 2

    return reverse_binary_string


def reverse_string(input_string):
    """Reverses a string. Used to reverse binary string from integer_to_reverse_binary function."""
    binary_string = ''
    for digit in reversed(input_string):
        binary_string += digit

    return binary_string


user_input = int(input())

binary = integer_to_reverse_binary(user_input)

print(binary)
print(reverse_string(binary))