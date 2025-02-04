# def swap_adjacent(s):
    """Swaps adjacent characters in a string by managing pointers (indices).

    Args:
        s: The input string.

    Returns:
        The string with adjacent characters swapped, or the original string
        if the length is less than 2.
    """

    if len(s) < 2:
        return s

    result = list(s)  # Convert to a list for mutability
    i = 0
    while i < len(result) - 1:
        result[i], result[i + 1] = result[i + 1], result[i]  # Swap
        i += 2  # Move to the next pair

    return "".join(result)  # Convert back to a string



# Test cases
input_string1 = "1234567890"
output_string1 = swap_adjacent(input_string1)
print(f"Input: '{input_string1}'")
print(f"Output: '{output_string1}'")

input_string2 = "AaBbCc"
output_string2 = swap_adjacent(input_string2)
print(f"Input: '{input_string2}'")
print(f"Output: '{output_string2}'")


input_string3 = "abc" #odd length
output_string3 = swap_adjacent(input_string3)
print(f"Input: '{input_string3}'")
print(f"Output: '{output_string3}'")


input_string4 = "ab" #even length
output_string4 = swap_adjacent(input_string4)
print(f"Input: '{input_string4}'")
print(f"Output: '{output_string4}'")

input_string5 = "a" #single char length
output_string5 = swap_adjacent(input_string5)
print(f"Input: '{input_string5}'")
print(f"Output: '{output_string5}'")


input_string6 = "" #empty string length
output_string6 = swap_adjacent(input_string6)
print(f"Input: '{input_string6}'")
print(f"Output: '{output_string6}'")
