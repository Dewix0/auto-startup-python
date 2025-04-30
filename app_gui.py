from tkinter import *
from tkinter import ttk,Listbox,font,filedialog


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("App closed")

 
def add_file():
    file_path = filedialog.askopenfilename(title="Choose file")
    status_var.set("Added new file,remember to save")
    label_status["fg"]="green"
    
    
def delete_file():
    status_var.set("File deleted") 
    label_status["fg"]="red" 
    
def save_file():
    status_var.set("Configuration saved")
    label_status["fg"]="green"  
    
#Запуска приложения
root = Tk()

#Определение центра экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Центрирование +-по размерам экрана
center_x=screen_width//2-300
center_y=screen_height//2-250

#Тестовый вывод
root.title("Anystart")
root.resizable(False, False)    
root.geometry(f"600x400+{center_x}+{center_y}")


custom_font = font.Font(size=15, weight="bold")    
label = Label(text="Run anything on windows startup",font=custom_font,anchor=N) 
label.pack()


status_var = StringVar()
status_var.set("Programm is running")
status_font=font.Font(weight="bold",size=12)
label_status=Label(textvariable=status_var,font=status_font,fg="blue")
label_status.pack(anchor=NW)

listbox =Listbox(root, selectmode=SINGLE)
listbox.pack(fill=BOTH, expand=True, padx=10, pady=10)


button_frame=ttk.Frame(borderwidth=15,relief=SOLID,padding=[10,12])

btn_add = ttk.Button(button_frame,text="Add file",command=add_file)
btn_add.pack(side=LEFT,padx=5)

btn_delete=ttk.Button(button_frame,text="Delete file",command=delete_file)
btn_delete.pack(side=LEFT,padx=5)

btn_save=ttk.Button(button_frame,text="Save file",command=save_file)
btn_save.pack(side=LEFT,padx=5)

button_frame.pack(side=BOTTOM)
root.protocol("WM_DELETE_WINDOW", finish)


root.mainloop()