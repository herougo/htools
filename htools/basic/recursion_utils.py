

def recursive_map(obj, fn):
    """ Recursive Transform
    Apply fn recursively on obj or descendents of obj which are not lists or tuples.
    
    TODO: proper documentation
    """
    
    if isinstance(obj, list):
        return [fn(x) for x in obj]
    elif isinstance(obj, tuple):
        return tuple([fn(x) for x in obj])
    else:
        return fn(obj)
