number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# This code generates a multiplication table for a given number.
# It prompts the user to input a number and then prints the multiplication results from 1 to 10.
# The use of f-strings allows for clear formatting of the output.