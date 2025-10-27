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
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\tkinter\__init__.py", line 1892, in __call__
    return self.func(*args)
  File "C:\Users\prashantVIT\PycharmProjects\SIH'23(Final Draft)\bknd.py", line 60, in Sensor
    send_whatsapp(excel_path, text_path, dmg, altr)
  File "C:\Users\prashantVIT\PycharmProjects\SIH'23(Final Draft)\bknd.py", line 26, in send_whatsapp
    df = pd.read_excel(data_file_excel, dtype={"Contact":str})
  File "C:\Users\prashantVIT\PycharmProjects\SIH'23(Final Draft)\venv\lib\site-packages\pandas\io\excel\_base.py", line 504, in read_excel
    io = ExcelFile(
  File "C:\Users\prashantVIT\PycharmProjects\SIH'23(Final Draft)\venv\lib\site-packages\pandas\io\excel\_base.py", line 1563, in __init__
    text="SUBMIT",
    padx=10,
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()C:\Users\prashantVIT\PycharmProjects\SIH'23(Draft)\test_io\test_f.mp4