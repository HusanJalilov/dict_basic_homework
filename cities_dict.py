def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
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
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))