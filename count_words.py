def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    count=0
    word=False
    for i in s:
        if i!=' ':
            if not word:
                word=True
                count+=1
        else:
            word=False
            
    return count
    
print(count_words("Hello world! How are you?"))