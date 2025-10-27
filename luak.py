from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2

model = YOLO('runs/detect/train4/weights/last.pt')
image = r"test_io\test_1.mp4"
res = model.predict(image, conf=0.5)
for result in res:
                boxes = result.boxes
                if len(boxes)!=0:
                    road.condition = 0