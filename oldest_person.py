import math
def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    # k=[]
    # s=people.values()
    # for x in s:
    #     k.append(x)
    # l=max(k)
    # if l in people.values():
    #     return people.values(l)    
    return max(people)
    
        
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))