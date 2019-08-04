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