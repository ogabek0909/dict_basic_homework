def last_item():
    """
    Given a dictionary, Return last item value.
    """
    data = {'a': 1, 'b': 2}
    k,v=data.popitem()
    return v
print(last_item())