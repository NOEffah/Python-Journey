def get_formatted_name(first, last, middle=''):
    """Generate neatly formatted name"""
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
        
    return fullname.title()