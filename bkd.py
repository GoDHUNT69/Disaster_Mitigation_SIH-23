from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2
from tkinter import *
from tkinter import ttk
import keyboard as k
import pyautogui
import webbrowser as web
import pandas as pd
import time
from urllib.parse import quote
import openpyxl


ws = Tk()
ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

model = YOLO('runs/detect/train4/weights/last.pt')

def send_whatsapp(data_file_excel, message_file_text, dmg, altr, x_cord=1728, y_cord=980):
    df = pd.read_excel(data_file_excel, dtype={"Contact":str})
    name = df['Name'].values
    contact = df['Contact'].values
    files = message_file_text
    with open(files) as f:
        file_data = f.read()
    zipped = zip(name,contact)
    counter = 0
    for (a,b) in zipped:
        msg = file_data.format(a, dmg, altr)
        web.open(f"https://web.whatsapp.com/send?phone={b}&text={quote(msg)}")
        time.sleep(15)
        pyautogui.click(x_cord,y_cord)
        time.sleep(2)
        k.press_and_release('enter')


        time.sleep(2)


        k.press_and_release('ctrl+w')

        time.sleep(1)

        counter +=1
        print(counter,"-Message sent...!!")

    print("Done!")




def Sensor_cam():
    res = model.predict(source=0, show=True, conf=0.5)
    for result in res:
        boxes = result.boxes
        if len(boxes) != 0:
            condition = 0
    if (condition == 0):
        altr = "Route 1"
        dmg = "Route 2"
        excel_path = r"C:\Users\Aditya Narayan\PycharmProjects\whatsapp\Book1.xlsx"
        text_path = r"C:\Users\Aditya Narayan\PycharmProjects\whatsapp\whatsapp draft.txt"
        send_whatsapp(excel_path, text_path, dmg, altr)

def Sensor():
    PATH = path.get()
    res = model.predict(source=PATH,show=True, conf=0.5)
    for result in res:
        boxes = result.boxes
        if len(boxes) != 0:
            condition=0
    if (condition == 0):
        altr = "Route 1"
        dmg = "Route 2"
        excel_path = r"C:\Users\Aditya Narayan\PycharmProjects\whatsapp\Book1.xlsx"
        text_path = r"C:\Users\Aditya Narayan\PycharmProjects\whatsapp\whatsapp draft.txt"
        send_whatsapp(excel_path, text_path, dmg, altr)
    else:
        pass

path = Entry(ws)
path.pack(pady=30)

Button(
    ws,
    text="Submit",
    padx=10,
    pady=5,
    command=Sensor
    ).pack()
Button(
    ws,
    text="Camera",
    padx=10,
    pady=5,
    command=Sensor_cam()
    ).pack()
ws.mainloop()
