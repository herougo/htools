

def recursive_map(obj, fn):
    """ Recursive Transform
    Apply fn recursively on obj or descendents of obj which are not lists or tuples.
    
    TODO: proper documentation
    """
    
    if isinstance(obj, list):
        return [recursive_map(x) for x in obj]
    elif isinstance(obj, tuple):
        return tuple([recursive_map(x) for x in obj])
    else:
        return fn(obj)

def recursive_all(obj, pred_fn):
    if isinstance(obj, (list, tuple)):
        for x in obj:
            if not recursive_all(x, pred_fn):
                return False

        return True
    else:
        return pred_fn(obj)


def recursive_any(obj, pred_fn):
    if isinstance(obj, (list, tuple)):
        for x in obj:
            if recursive_all(x, pred_fn):
                return True

        return False
    else:
        return pred_fn(obj)

