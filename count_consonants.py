def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    consonants="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    count=0
    for c in s:
        if c in consonants:
            count+=1

    return count
print(count_consonants("Arjun sharma"))
