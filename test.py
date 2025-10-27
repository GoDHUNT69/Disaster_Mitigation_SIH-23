from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2

model = YOLO('runs/detect/train4/weights/best.pt')
model.predict(source=r"C:\Users\prashantVIT\PycharmProjects\SIH'23(Draft)\test_io\test_f.mp4", show=True, conf=0.5)

while(True):
    pass