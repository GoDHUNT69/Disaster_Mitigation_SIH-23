import keyboard as k
import pyautogui
import webbrowser as web
import pandas as pd
import time
from urllib.parse import quote
import openpyxl

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

excel_path = r"C:\Users\prashantVIT\PycharmProjects\SIH'23(Final Draft)\whatsapp\Book1.xlsx"
text_path = r"C:\Users\prashantVIT\PycharmProjects\SIH'23(Final Draft)\whatsapp\whatsapp draft.txt"
x="GT road"
y="MG Road"
send_whatsapp(excel_path,text_path,dmg=x,altr=y)

