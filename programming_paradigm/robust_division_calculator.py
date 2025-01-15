def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers with error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: Formatted result string or error message
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            raise ZeroDivisionError
            
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: non-numeric input"
    except ZeroDivisionError:
        return "Error: division by zero"