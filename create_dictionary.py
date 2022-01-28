def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    
    
    res = {}
    for i in key:
        for j in value:
            res[i] = j
            value.remove(j)
            break  
    return res 
print(create_dictionary([1,2,3],["one","two","three"]))



# key = [1, 2, 3] value = ["one", "two", "three"]
# {1: "one", 2: "two", 3: "three"}