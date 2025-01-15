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
    
    try:
        # Perform division
        result = safe_divide(numerator, denominator)
        print(f"The result of the division is {result}")
        sys.exit(0)
        
    except ValueError:
        print("Error: non-numeric input")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: division by zero")
        sys.exit(1)

if __name__ == "__main__":
    main()