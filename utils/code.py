def is_programming_related(text):
    """
    Determine if the provided text is related to programming concepts.

    This function checks the input text for the presence of common programming-related keywords. 
    If any of the keywords are found, it returns True, indicating that the text is likely 
    related to programming. Otherwise, it returns False.

    Args:
        text (str): The text input to analyze for programming-related keywords.

    Returns:
        bool: True if the text contains any programming-related keywords; False otherwise.
    """
    keywords = ['def', 'class', 'import', 'function', 'syntax', 'error', 'variable', 'loop', 'condition', 'array', 'list', 'object', 'method']
    return any(keyword in text for keyword in keywords)
