from collections import OrderedDict
def remove_duplicates(s):
    
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here 
    return "".join(OrderedDict.fromkeys(s)) 
print(remove_duplicates("Hello World"))
        
