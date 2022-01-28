def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    
    test_values=[]
    for i in range(len(cities)):
        test_values.append(i) 
    res = {}
    for key in cities:
        for value in test_values:
            res[value] = key
            test_values.remove(value)
            break  
    return res 



# key = [1, 2, 3] value = ["one", "two", "three"]
# {1: "one", 2: "two", 3: "three"}