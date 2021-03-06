def v(var):
	"""
	A function for visualizing the variable var
	"""
	attrs = dir(var)
	d = {key: getattr(var, key) for key in attrs}
	for key, val in d.items():
		print(key, val)

# ML
import numpy as np

def loguniform(lower, upper):
    return 2 ** np.random.uniform(np.log2(lower), np.log2(upper))

def sigmoid(x):
    return 1 / (1 + np.exp(-1 * x))

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=-1).reshape(tuple(x.shape[:2]) + (1,))


def split_tvt(data, split, lengths=None):
    """
    Example:
    n_data_points = 3
    input_len = 14
    data = np.zeros((n_data_points, input_len))
    split = [0.6, 0.2, 0.2]  # [train_ratio, val_ratio, test_ratio] sums to 1
    lengths = [3, 1, 1]  # weights for each row in data when determining the split
    train, val, test = split_tvt(data, split, lengths)
    assert [len(split) == 1 for split in [train, val, test]] # due to length weighting

    TODO: improve documentation
    """
    assert len(split) == 3
    data_len = len(data)
    if lengths is None:
        val_start = int(data_len * split[0])
        test_start = val_start + int(data_len * split[1])
    else:
        acc_sum = 0
        total_sum = sum(lengths)
        val_start_sum = int(total_sum * split[0])
        test_start_sum =  val_start_sum + int(total_sum * split[1])
        for i in range(data_len):
            acc_sum += data[i]
            if acc_sum >= val_start_sum:
                val_start = i
                break

        test_start = val_start
        for i in range(val_start_sum + 1, data_len):
            acc_sum += data[i]
            if acc_sum >= test_start_sum:
                test_start = i
                break
    
    return data[:val_start], data[val_start:test_start], data[test_start:]

# ALGORITHMS


def fn_binary_search(fn, lower, upper, target):
    # lower <= x < upper
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = fn(x)
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

    return -1

# OTHER

import inspect
import warnings

def unnecessary_wrapper(func):
    def warn_and_call(*args, **kwargs):
        source_code = inspect.getsource(func)
        warnings.warn('{} is unnecessary. Use this code instead:\n{}'.format(
            func.__name__, source_code))
        return func(*args, **kwargs)
    return authenticate_and_call



def readable_sec(seconds):
    """
    :param seconds: int seconds
    :returns: string e.g. 12 days, 4 hours, 3 min, 4 sec
    """
    c = int(c)
    days = (c // 86400)
    hours = (c // 3600) % 24
    minutes = (c // 60) % 60
    seconds = c % 60
    result = ""
    if days > 0:
        result += str(days) + " days, "
    if hours > 0:
        result += str(hours) + " hrs, "
    if minutes > 0:
        result += str(minutes) + " min, "
    result += str(seconds) + " sec"
    return result

def normalize(arr):
    arr = np.array(arr)
    return (arr - np.mean(arr)) / np.std(arr)

from google.protobuf import text_format
def parse_from_text_plain_string(empty_proto, text: str):
    return text_format.Merge(text, empty_proto)  # returns empty_proto (which was modified)

import datetime
def date_to_human_readable(date):
    # returns e.g. "Aug-22-2019"
    month_name = date.strftime("%B")
    return '{}-{}-{}'.format(month_name[:3], date.day, date.year)

def num_to_string_n_decimal_places(number, n):
    return '%.{}f'.format(n) % number

