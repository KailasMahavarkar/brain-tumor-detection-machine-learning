FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
RUN apk add g++
RUN pip install flask flask-cors
RUN pip install matplotlib numpy
RUN pip install -U scikit-learn

RUN pip install keras
RUN pip install tensorflow
RUN pip install opencv-python

COPY . .
EXPOSE 5000
RUN python3 app.py