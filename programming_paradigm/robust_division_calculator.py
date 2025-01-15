def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers with error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        float: Result of division if successful
        
    Raises:
        ValueError: If inputs cannot be converted to float
        ZeroDivisionError: If denominator is zero
    """
    try:
        # Convert inputs to float - may raise ValueError
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            raise ZeroDivisionError("Cannot divide by zero")
            
        # Perform division
        result = num / den
        return result
        
    except (ValueError, ZeroDivisionError):
        # Re-raise the exceptions to be handled by the caller
        raise