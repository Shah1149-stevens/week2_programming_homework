import re

def is_palindrome(s):
  """
  Checks if a string is a palindrome, ignoring case and non-letter characters.

  Args:
    s: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Remove non-letter characters and convert to lowercase
  s = re.sub(r'[^a-zA-Z]', '', s).lower()
  return s == s[::-1]

# Example usage:
input_string = "Taco cat" 
if is_palindrome(input_string):
  print(f"'{input_string}' is a palindrome.")
else:
  print(f"'{input_string}' is not a palindrome.")

input_string = "I Love DSA"
if is_palindrome(input_string):
  print(f"'{input_string}' is a palindrome.")
else:
  print(f"'{input_string}' is not a palindrome.")
