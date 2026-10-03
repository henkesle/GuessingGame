def is_valid_target(value):
    """Check if a value is a valid game target (odd integer between 1 and 1000)."""
    # Check if value is an integer
    if not isinstance(value, int):
        return False
    
    # Check if value is in range [1, 1000]
    if value < 1 or value > 1000:
        return False
    
    # Check if value is odd
    if value % 2 == 0:
        return False
    
    return True
