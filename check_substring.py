def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    len_s = 0
    len_t = 0
    while s[len_s:]:
        len_s += 1
    while t[len_t:]:
        len_t += 1
    if len_t > len_s:
        return False
    for i in range(len_s - len_t + 1):
        j = 0
        while j < len_t and s[i + j] == t[j]:
            j += 1
        if j == len_t:
            return True
 
    return False
    
print(is_substring("hello world","world"))
