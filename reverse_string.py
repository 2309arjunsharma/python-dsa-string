def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here
    r=""
    for i in range(len(s)-1,-1,-1):
        r+=s[i]
        
    return r
    
print(reverse_string("Python"))
