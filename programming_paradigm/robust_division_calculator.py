def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers with error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        float: Result of division if successful
        str: Error message if division cannot be performed
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
            
        # Perform division
        result = num / den
        return result
        
    except ValueError:
        return "Error: Please provide numeric inputs"
    except ZeroDivisionError as e:
        return str(e)
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"