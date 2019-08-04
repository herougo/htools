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

