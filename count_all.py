def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    s=[]
    d=[]
    for x in txt:
        if x.isdigit():
            s.append(x)
        elif not x.isdigit():
            if x!=" ":
                d.append(x)
    b={"LETTERS":len(d),"DIGITS":len(s)}
            
    return b
    
            
        
print(count_all("Hello World"))