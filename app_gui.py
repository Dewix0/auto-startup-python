from tkinter import *
from tkinter import ttk


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("App closed")


clicks = 0
 
def click_button():
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    btn["text"] = f"Clicks {clicks}" 
#Запуска приложения
root = Tk()

#Определение центра экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Центрирование +-по размерам экрана
center_x=screen_width//2-150
center_y=screen_height//2 -200

#Тестовый вывод
root.title("Anystart")
root.resizable(False, False)    
root.geometry(f"500x300+{center_x}+{center_y}")    
label = Label(text="Run app on windows startup") 
label.pack()


btn = ttk.Button()

btn["text"]="Path"
btn["command"]=click_button
btn.pack()


root.protocol("WM_DELETE_WINDOW", finish)
