import numpy as np
import wikipedia
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential,Model,model_from_json
from keras.layers import Conv2D,MaxPooling2D,Dense,Dropout,Flatten
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import glob
import keras
from keras.applications import vgg16
from keras.layers import Input
import matplotlib.pyplot as plt
import env
import os
import cv2
from contextlib import suppress

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
        return float(predicted_result[0][0])
    return float(-1)



if __name__ == '__main__':
    result = ModelPredictor()
    print(result)