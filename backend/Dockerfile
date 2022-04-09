FROM ubuntu
RUN apt update -y
RUN apt install -y libgl1-mesa-glx
RUN apt install wget -y
RUN apt install g++ -y
RUN apt install python3-pip -y
RUN wget "https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.8.0-cp38-cp38-manylinux2010_x86_64.whl" -O tensorflow_cpu-2.8.0-cp38-cp38-manylinux2010_x86_64.whl
RUN pip install tensorflow_cpu-2.8.0-cp38-cp38-manylinux2010_x86_64.whl
RUN pip install flask flask-cors matplotlib numpy
RUN pip install -U scikit-learn
RUN pip install opencv-python
RUN pip install ffmpeg
RUN apt install libsm6 -y
RUN apt install libxext6 -y
COPY . .
EXPOSE 5000
RUN python3 app.py