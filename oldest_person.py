def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    k1,v1=people.popitem()
    
    for k,v in people.items():
        if v1<v:
            v1=v
            k1=k
    return k1
print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 56}))
    