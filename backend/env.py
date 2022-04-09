import os


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STORAGE_PATH = os.path.join(ROOT_PATH, 'storage')
MODEL_PATH = os.path.join(STORAGE_PATH, 'model.json')
MODEL_H5_PATH = os.path.join(STORAGE_PATH, 'model.h5')
TEMP_PATH = os.path.join(STORAGE_PATH, 'temp.jpg')