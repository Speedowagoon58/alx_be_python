def safe_divide(numerator, denominator):
    # Convert inputs to float
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")
    
    # Perform division
    if den == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero")
    
    result = num / den
    return f"The result of the division is {result}"

"""
Error: Cannot divide by zero.

"""