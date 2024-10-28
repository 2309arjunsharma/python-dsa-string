def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    if len(s)!=len(t):
        return False
    len_s=[0]*26
    len_t=[0]*26
    for k in s:
        len_s[ord(k)-ord('a')]+=1
    for j in t:
        len_t[ord(j)-ord('a')]+=1   
    for i in range(26):
        if len_s[i]!=len_t[i]:
            return False
            
    return True
print(is_anagram("anagram","nagaram"))
    
