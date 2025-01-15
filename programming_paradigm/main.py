import sys
from robust_division_calculator import safe_divide

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)
    
    # Get arguments from command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform division and handle result
    result = safe_divide(numerator, denominator)
    
    # Output formatting
    if isinstance(result, str):
        print(result)
        sys.exit(1)
    else:
        print(f"The result of the division is {result}")
        sys.exit(0)

if __name__ == "__main__":
    main()