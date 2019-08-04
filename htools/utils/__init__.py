import sys

class AttrDict(dict):
    ''' https://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute '''
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def get_input_lines():
    if sys.version_info[0] < 3:
        lines = raw_input().split('\n')
    else:
        lines = input().split('\n')



# UNNECESSARY WRAPPERS

def round_number(n, n_decimal_places):
    return round(n, n_decimal_places)

def get_python_version():
    """
    :return: float I think?
    """
    return sys.version_info[0]