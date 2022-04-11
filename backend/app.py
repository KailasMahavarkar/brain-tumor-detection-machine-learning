from flask import Flask,  request, jsonify
from flask_cors import CORS
from contextlib import suppress
import os
import cv2
import numpy as np

from Model import ModelPredictor

app = Flask(__name__)
cors = CORS(app)


@app.route('/scan', methods=['POST'])
def runREQ():
    with suppress(Exception):
        if request.files.to_dict(flat=False)['file']:
            xfile = request.files['file']
            
            npArray = np.fromstring(xfile.read(), np.uint8)
            img = cv2.imdecode(npArray, cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img,(224,224))
            img = np.reshape(img,[1,224,224,3])
            
            modelResult = ModelPredictor(img=img)
            
            
            if modelResult != -1:
                return jsonify({
                    "msg": "model prediction was success",
                    "success": "success",
                    "prediction": ModelPredictor(img=img)
                })
            else:
                return jsonify({
                    "msg": "model prediction was null",
                    "success": "failed",
                    "prediction": -1
                })
    
    return jsonify({
        "msg": "could not upload image",
        "success": "exited",
        "error": "Server Error"
    })


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "msg": "Welcome to Braintumor detection API",
        "success": "success"
    })


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def allroutes(u_path):
    return jsonify({
        "msg": "bad request",
        "success": "failed",
        "error": "404 | url not found",
    })


if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)


