from keras import backend as K

def build_network(**params):
    from keras.models import Model
    from keras.layers import Input, Conv1D, BatchNormalization, Activation, Add, MaxPooling1D, Dropout
    from keras.layers.core import Lambda, Dense
    #from keras.layers.core import Activation
    from keras.layers.wrappers import TimeDistributed
    from keras.optimizers import Adam
    
    def zeropad(x):
        y = K.zeros_like(x)
        return K.concatenate([x, K.zeros_like(x)], axis=2)

    def zeropad_output_shape(input_shape):
        shape = list(input_shape)
        assert len(shape) == 3
        shape[2] *= 2
        return tuple(shape)

    inputs = Input(shape=[None, 1], dtype='float32', name='inputs')

    # 1st Conv layer (number of filters = 32)
    layer = Conv1D(filters=32, kernel_size=16 , strides=1, padding='same', kernel_initializer='he_normal')(inputs)
    layer = BatchNormalization()(layer)
    layer = Activation(params["conv_activation"])(layer)


    # 0th resnet layer (number of filters = 32, subsampling = 1)
    shortcut_0 = MaxPooling1D(pool_size=1)(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_0, layer])

    # 1st resnet layer (number of filters = 32, subsampling = 2) 
    shortcut_1 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_1, layer])

    # 2nd resnet layer (number of filters = 32, subsampling = 1)
    shortcut_2 = MaxPooling1D(pool_size=1)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_2, layer])

    # 3rd resnet layer (number of filters = 32, subsampling = 2)
    shortcut_3 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=32, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_3, layer])

    # 4th resnet layer (number of filters = 64, subsampling = 1, zero-pad)
    shortcut_4 = MaxPooling1D(pool_size=1)(layer)
    shortcut_4 = Lambda(zeropad, output_shape=zeropad_output_shape)(shortcut_4)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_4, layer])

    # 5th resnet layer (number of filters = 64, subsampling = 2)
    shortcut_5 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_5, layer])

    # 6th resnet layer (number of filters = 64, subsampling = 1)
    shortcut_6 = MaxPooling1D(pool_size=1)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_6, layer])
    
    # 7th resnet layer (number of filters = 64, subsampling = 2)
    shortcut_7 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=64, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_7, layer])
    
    # 8th resnet layer (number of filters = 128, subsampling = 1, zero-pad)
    shortcut_8 = MaxPooling1D(pool_size=1)(layer)
    shortcut_8 = Lambda(zeropad, output_shape=zeropad_output_shape)(shortcut_8)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_8, layer])
    
    # 9th resnet layer (number of filters = 128, subsampling = 2)
    shortcut_9 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_9, layer])

    # 10th resnet layer (number of filters = 128, subsampling = 1)
    shortcut_10 = MaxPooling1D(pool_size=1)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_10, layer])
    
    # 11th resnet layer (number of filters = 128, subsampling = 2)
    shortcut_11 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=128, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_11, layer])

    # 12th resnet layer (number of filters = 256, subsampling = 1, zero-pad)
    shortcut_12 = MaxPooling1D(pool_size=1)(layer)
    shortcut_12 = Lambda(zeropad, output_shape=zeropad_output_shape)(shortcut_12)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_12, layer])
    
    # 13th resnet layer (number of filters = 256, subsampling = 2)
    shortcut_13 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_13, layer])
    
    # 14th resnet layer (number of filters = 256, subsampling = 1)
    shortcut_14 = MaxPooling1D(pool_size=1)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_14, layer])

    # 15th resnet layer (number of filters = 256, subsampling = 2)
    shortcut_15 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=256, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_15, layer])
    
    
    #####################################  추가됨  ##########################################
    
    '''
    # 16th resnet layer (number of filters = 256, subsampling = 1, zero-pad)
    shortcut_16 = MaxPooling1D(pool_size=1)(layer)
    shortcut_16 = Lambda(zeropad, output_shape=zeropad_output_shape)(shortcut_16)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_16, layer])
    
    # 17th resnet layer (number of filters = 256, subsampling = 2)
    shortcut_17 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_17, layer])
    
    # 18th resnet layer (number of filters = 256, subsampling = 1)
    shortcut_18 = MaxPooling1D(pool_size=1)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_18, layer])
    
    # 19th resnet layer (number of filters = 256, subsampling = 2)
    shortcut_19 = MaxPooling1D(pool_size=2)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=2, padding='same', kernel_initializer='he_normal')(layer)
    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.2)(layer)
    layer = Conv1D(filters=512, kernel_size=16, strides=1, padding='same', kernel_initializer='he_normal')(layer)
    layer = Add()([shortcut_19, layer])
    '''

    layer = BatchNormalization()(layer)
    layer = Activation('relu')(layer)

    #Output layer (number of output = class number)
    layer = TimeDistributed(Dense(params["num_categories"]))(layer)
    output = Activation('softmax')(layer)

    model = Model(inputs=[inputs], outputs=[output])

    optimizer = Adam(lr=params["learning_rate"])
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    
    return model
