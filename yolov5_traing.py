# -*- coding: utf-8 -*-
"""yolov5-Train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VWEfOf5_jgT5zIoIyvqYQKR2IMZPZOhK
"""

!nvidia-smi

!git clone https://github.com/ultralytics/yolov5.git

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov5/
!pip install -r requirements.txt

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="cpOUyBbgcmT9hwQG19ej")
project = rf.workspace("kripya-solutions").project("summa-uxs0d")
dataset = project.version(1).download("yolov5")

!python train.py --data coco128.yaml --epochs 10 --weights '' --cfg yolov5x.yaml  --batch-size 128