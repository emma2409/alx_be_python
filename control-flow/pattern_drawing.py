# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to control rows
while row < size:
    # Use for loop to print each column of asterisks
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1
