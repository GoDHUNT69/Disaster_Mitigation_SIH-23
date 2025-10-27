import os
import torch
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")
model.train(data='config.yaml', epochs=7)