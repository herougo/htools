# ML

def loguniform(low, high):
    low = np.log10(low)
    high = np.log10(high)
    return 10 ** np.random.uniform(low, high)

# Keras

def binary_crossentropy(y_true, y_pred):
    """ Notes
    - y_true shape == y_pred shape
      - b/c keras.backend.binary_crossentropy documentation
    - def binary_crossentropy(y_true, y_pred):
          return K.mean(K.binary_crossentropy(y_true, y_pred), axis=-1)
    - K.binary_crossentropy(y_true, y_pred) returns tensor of same shape as inputs
      - b/c of tf.nn.sigmoid_cross_entropy_with_logits documentation
    """
    return keras.losses.binary_crossentropy(y_true, y_pred)



def smoothL1(y_true, y_pred):
    # https://en.wikipedia.org/wiki/Huber_loss
    # https://stackoverflow.com/questions/44130871/keras-smooth-l1-loss
    huber_delta = 1
    x   = K.abs(y_true - y_pred)
    x   = K.switch(x < huber_delta, 0.5 * x ** 2, huber_delta * (x - 0.5 * huber_delta))
    return  K.mean(x)

# ML VISUALIZATION

def plot_one_value_search(hyp, scores):
    """
    Plot results after one value search for hyperparameter search
    :param hyp: list of dict representing hyperparameter configurations
    :param scores: list of numbers representing the metric values for each
                   hyperparameter configuration in hyp
    """
    if len(hyp) != len(scores):
        raise Exception('len(hyp) != len(scores)')
    
    keys = list(hyp[0].keys())
    
    key = keys[0]
    most_common_value = list(dict(Counter([d[key] for d in hyp]).most_common(1)).keys())[0]
    # find instance where it doesn't have the most common value
    
    ix_w_not_common = None
    for i, d in enumerate(hyp):
        if d[key] != most_common_value:
            ix_w_not_common = i
            break
    if ix_w_not_common is None:
        raise Exception('invalid hyp argument')
    
    base_config = hyp[ix_w_not_common].copy()
    base_config[key] = most_common_value
    
    ix_base_config = None
    for i, d in enumerate(hyp):
        if d == base_config:
            ix_base_config = i
            break
            
    if ix_base_config is None:
        raise Exception('invalid hyp argument: missing expected base configuration' + 
            f'{base_config}')
        
    for key in keys:
        other_keys = set(keys) - set([key])
        key_config_ids = [i for i, d in enumerate(hyp) 
                          if all([d[other_key] == base_config[other_key] 
                                  for other_key in other_keys])]
        expected_n_ids = len(set([d[key] for d in hyp]))
        
        print(f'{len(key_config_ids)} ids for {key}')
        #assert len(key_config_ids) == expected_n_ids, [hyp[i] for i in key_config_ids]

        x = [hyp[i][key] for i in key_config_ids]
        y = [scores[i] for i in key_config_ids]
        pw.scatter(x, y, title=f'{key} results', x_label=key, y_label='score')

# Elastic Search

from elasticsearch import Elasticsearch

def es_query(host, index, body, doc_type, get, match, result, port=9200, size=1000):
    def append_to_results(hits):
        for item in hits:
            use = True
            if match is not None:
                for keys, val in match:
                    keys_result = item
                    for key in keys:
                        keys_result = keys_result[key]
                    if keys_result != val:
                        use = False
                        break
            if use:
                new_entry = {}
                for keys in get:
                    keys_result = item
                    for key in keys:
                        keys_result = keys_result[key]
                    new_entry[key] = keys_result
                result.append(new_entry)
            
    
    timeout = 1000
    es = Elasticsearch([{'host': host, 'port': port}], timeout=timeout)
    if not es.indices.exists(index=index):
        print("Index " + index + " not exists")
        exit()
    data = es.search(index=index, doc_type=doc_type, 
                     scroll='2m', size=size, body=body)
    sid = data['_scroll_id']
    scroll_size = len(data['hits']['hits'])
    counter = scroll_size
    
    while scroll_size > 0:
        print(f"Scrolling...(after {counter})")
        data = es.scroll(scroll_id=sid, scroll='20m')

        # Process current batch of hits
        append_to_results(data['hits']['hits'])

        # Update the scroll ID
        sid = data['_scroll_id']

        # Get the number of results that returned in the last scroll
        scroll_size = len(data['hits']['hits'])
        counter += scroll_size
        
    print("done")

# OTHER




# UNSORTED

def is_same_price(float1, cloat2):
  return abs(float1 - float2) <= 0.0001

def is_protobuf(var):
    # is this correct?
    from google.protobuf.message import Message
    return isinstance(var, Message)

def is_repeatable_protobuf(var):
    # is this correct?
    return is_protobuf(var) and hasattr(var, 'add')

def dump_protobuf(obj):
    for descriptor in obj.DESCRIPTOR.fields:
        value = getattr(obj, descriptor.name)
        if descriptor.type == descriptor.TYPE_MESSAGE:
            if descriptor.label == descriptor.LABEL_REPEATED:
                map(dump_object, value)
            else:
                dump_object(value)
        elif descriptor.type == descriptor.TYPE_ENUM:
            enum_name = descriptor.enum_type.values[value].name
            print("%s: %s" % (descriptor.full_name, enum_name))
        else:
            print("%s: %s" % (descriptor.full_name, value))


def iter_recursive_protobuf_fields(obj):
    # stackoverflow
    for descriptor in obj.DESCRIPTOR.fields:
        value = getattr(obj, descriptor.name)
        if descriptor.type == descriptor.TYPE_MESSAGE:
            if descriptor.label == descriptor.LABEL_REPEATED:
                for val in value:
                    for result in iter_recursive_protobuf_fields(val):
                        yield result
            else:
                for result in iter_recursive_protobuf_fields(value):
                    yield result
        elif descriptor.type == descriptor.TYPE_ENUM:
            enum_name = descriptor.enum_type.values[value].name
            yield descriptor.full_name, enum_name, True
        else:
            yield descriptor.full_name, value, False

def dump_protobuf(obj):
    for full_name, value, is_enum in iter_recursive_protobuf_fields(obj):
        print('{}: {}'.format(full_name, value))
    


def iter_recursive_protobuf_fields(obj):
    # inefficient
    def iter_recursive_protobuf_fields_helper(obj, full_name_path):
        for descriptor in obj.DESCRIPTOR.fields:
            value = getattr(obj, descriptor.name)
            if descriptor.type == descriptor.TYPE_MESSAGE:
                if descriptor.label == descriptor.LABEL_REPEATED:
                    full_path = '{}.{}'.format(full_name_path, descriptor.name)
                    yield full_path, descriptor.name, value, False
                    for i, val in enumerate(value):
                        full_path = '{}.{}[{}]'.format(full_name_path, descriptor.name, i)
                        descriptor_name = '{}[{}]'.format(descriptor.name, i)
                        yield full_path, descriptor_name, val, False
                        for result in iter_recursive_protobuf_fields_helper(val, full_path):
                            yield result
                else:
                    full_path = '{}.{}'.format(full_name_path, descriptor.name)
                    yield full_path, descriptor.name, value, False
                    for result in iter_recursive_protobuf_fields_helper(value, full_path):
                        yield result
            elif descriptor.type == descriptor.TYPE_ENUM:
                enum_name = descriptor.enum_type.values[value].name
                yield full_name_path, descriptor.name, enum_name, True
            else:
                yield full_name_path, descriptor.name, value, False
    
    for result in iter_recursive_protobuf_fields_helper(obj, ''):
        yield result


def lazy_proto_get(obj, key, where=None, default=None):
    #global dbg_keys_seen
    #dbg_keys_seen = set()
    def lazy_get_yield(obj, key, where=None):
        if isinstance(obj, dict):
            if key in obj:
                if where is None or dict_subset_of(where, obj):
                    yield obj[key]
            else:
                for val in obj.values():
                    for result in lazy_get_yield(val, key, where):
                        yield result
        elif isinstance(obj, (list, tuple)):
            for val in obj:
                for result in lazy_get_yield(val, key, where):
                    yield result
        elif is_protobuf(obj):
            for _, proto_key, proto_value, _ in iter_recursive_protobuf_fields(obj):
                #dbg_keys_seen.add(proto_key)
                if proto_key == key:
                    yield proto_value
        
    results = list(lazy_get_yield(obj, key, where))
    if len(results) == 0:
        return default
    return results[0]


def my_log2(file_type, arg):
    # logs output to a file in a useful manner
    # TODO: Save to directory by date

    # import pprint
    # pprint.PrettyPrinter(indent=2).pprint(*args)

    file_path = f'/Users/hromel/temp/logs/high_detail_search/1_{file_type}_log.txt'
    f = open(file_path, 'w')
    f.write(str(arg) + '\n')
    f.close()


def my_log(file_type, arg, type='w'):
    # logs output to a file in a useful manner
    # TODO: Save to directory by date

    # import pprint
    # pprint.PrettyPrinter(indent=2).pprint(*args)

    file_path = f'/Users/hromel/temp/logs/prebook/1_{file_type}_log.txt'
    f = open(file_path, type)
    import pprint
    text = pprint.pformat(arg, indent=4)
    f.write(text  + '\n')
    f.close()

def get_log(file_type):
    # logs output to a file in a useful manner
    # TODO: Save to directory by date

    # import pprint
    # pprint.PrettyPrinter(indent=2).pprint(*args)

    file_path = f'/Users/hromel/temp/logs/prebook/1_{file_type}_log.txt'
    return file_to_string(file_path)

def example_remove_python_variable_from_global_scope():
    global x
    x = 0
    d = [x]
    del x
    # x is undefined, but d still has access to it



