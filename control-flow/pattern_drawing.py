# pattern_drawing.py

# Get input from user
size = int(input("Enter the size of the pattern: "))

# Initialize counter for the while loop
row = 0

# Use while loop to iterate through rows
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    
    # Print newline after each row is complete
    print()
    
    # Increment row counter
    row += 1