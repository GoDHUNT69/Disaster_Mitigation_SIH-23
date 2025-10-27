from tkinter import *
from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2


ws = Tk()
ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

def printValue():
    pname = player_name.get()
    model = YOLO('runs/detect/train4/weights/last.pt')
    X = pname
    model.predict(source=X, show=True, conf=0.5)
    res = model.predict(image, conf=conf)
    for result in res:
        boxes = result.boxes
        if len(boxes) == 0:
            print("no detections")


player_name = Entry(ws)
player_name.pack(pady=30)

Button(
    ws,
    text="SUBMIT",
    padx=10,
    pady=5,
    command=printValue
    ).pack()
Button(
    ws,
    text="SUBMIT",
    padx=10,
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()