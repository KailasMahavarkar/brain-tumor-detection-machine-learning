import numpy as np
from keras.models import model_from_json
import env
import os
import cv2
from contextlib import suppress
from Cleaner import ModelPredictor_

import tensorflow as tf

# switch to cpu if gpu is unavailable in the system
if (len(tf.config.experimental.list_physical_devices('GPU'))) < 1:
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


def imageLoader(path=''):
    img = cv2.imread(path)
    img = cv2.resize(img,(224,224))
    img = np.reshape(img,[1,224,224,3])
    return img


def ModelPredictor(img: any) -> float:
    with suppress(Exception):
        json_file = open(env.MODEL_PATH, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
                
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(env.MODEL_H5_PATH)
        loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        
        predicted_result = (loaded_model.predict(img) > 0.5).astype("int32")
        return predicted_result
    return float(-1)



if __name__ == '__main__':
    result = ModelPredictor()
    print(result)