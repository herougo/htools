import numpy as np
import inspect

def is_number(var):
	try:
		float(val)
	except:
		return False


def is_number_v2(var):
    return isinstance(np.isfinite(var), np.bool_)

def is_class(var):
    return inspect.isclass(var)

def is_function(var):
    return callable(var)