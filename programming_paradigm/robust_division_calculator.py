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
    # Convert inputs to float
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")
    
    # Perform division
    if den == 0:
        raise ZeroDivisionError("Error: division by zero")
    
    result = num / den
    return f"The result of the division is {result}"