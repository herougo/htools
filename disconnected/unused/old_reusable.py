

def pkl_save_all(file_path, l):
    with open(file_path, 'wb') as f:
        for val in l:
            pickle.dump(val, f)

def pkl_load_all(file_path):
    with open(file_path, 'rb') as f:
        l = []
        try:
            while True:
                l.append(pickle.load(f))
        except:
            pass

    return l

def mymap(fn, l):
    warnings.warn("Use [ ... for x in l syntax instead]")
    if isinstance(fn, (dict, list)):
        return [fn[val] for val in l]
    else:
        return list(map(fn, l))

def myfilter(fn, l):
    return list(filter(fn, l))

hmodels = '/Users/hromel/models/'
hdata = '/Users/hromel/data/'
hresults = '/Users/hromel/Documents/ml_results/'
tflogs = '/Users/hromel/tf_logs/'

def amap(att, l):
    try:
        return list(map(lambda x: x.__getattribute__(att), l))
    except AttributeError as ex:
        for val in l:
            attributes = dir(val)
            assert att in attributes, '{} not in {}'.format(att, attributes)
