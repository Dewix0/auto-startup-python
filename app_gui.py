from tkinter import *


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
root.geometry(f"500x300+{center_x}+{center_y}")    
label = Label(text="Run app on windows startup") 
label.pack()
root.mainloop()