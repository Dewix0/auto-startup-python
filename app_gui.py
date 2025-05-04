from tkinter import *
from tkinter import ttk, Listbox, font, filedialog
import json
import os


# хранение программ
programs = []

# Загрузка сохраненных программ из json
CONFIG_FILE = os.path.join(os.getenv("APPDATA"), "pet_app_config.json")
STARTUP_PATH = os.path.join(
    os.getenv("APPDATA"),
    "Microsoft",
    "Windows",
    "Start Menu",
    "Programs",
    "Startup",
    "easy_start.bat",
)


def start():
    global programs
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as fh:
                programs = json.load(fh)
        except Exception as e:
            print(f"Configuration load failed : {str(e)}")
    listboxupdater()


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("App closed")


# Сохранение добавленных программ в json, а так-же в запускаемый bat файл на старте windows
def save_configuration():
    try:
        with open(CONFIG_FILE, "w") as fh:
            json.dump(programs, fh)
            
        
        with open(STARTUP_PATH, "w", encoding="cp866") as bt:
            for program in programs:
                win_path = program.replace("/", "\\")
                bt.write(f'start "" "{win_path}"\n')
    except Exception as e:
        print(f"Failed to save conf : {str(e)}")


# Обновление программ в listbox
def listboxupdater():
    listbox.delete(0, END)
    for program in programs:
        listbox.insert(END, program)


def add_file():
    file_path = filedialog.askopenfilename(title="Choose file")
    if file_path:
        programs.append(file_path)
        listboxupdater()
        status_var.set("Added new file, remember to save conf")
        label_status["fg"] = "green"


def delete_file():
    selection = listbox.curselection()
    if selection:
        programs.pop(selection[0])
        listboxupdater()
        status_var.set("File deleted , remember to save conf")
        label_status["fg"] = "red"


def save_file():
    status_var.set("Configuration saved")
    save_configuration()
    label_status["fg"] = "green"


def app_init():
    # Запуска приложения
    global listbox
    global root
    global status_var
    global label_status
    root = Tk()

    # Определение центра экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Центрирование +-по размерам экрана
    center_x = screen_width // 2 - 300
    center_y = screen_height // 2 - 250

    # конфигурация окна приложения
    root.title("Anystart")
    root.resizable(False, False)
    root.geometry(f"600x400+{center_x}+{center_y}")

    # Заголовок
    custom_font = font.Font(size=15, weight="bold")
    label = Label(text="Run anything on windows startup", font=custom_font, anchor=N)
    label.pack()

    # статус бар
    status_var = StringVar()
    status_var.set("Programm is running")
    status_font = font.Font(weight="bold", size=12)
    label_status = Label(textvariable=status_var, font=status_font, fg="blue")
    label_status.pack(anchor=NW)

    # окно,где будет указываться путь сохранненых файлов
    listbox = Listbox(root, selectmode=SINGLE)
    listbox.pack(fill=BOTH, expand=True, padx=10, pady=10)
    return root


# фрейм с кнопками
def button_init():
    button_frame = ttk.Frame(borderwidth=15, relief=SOLID, padding=[10, 12])

    btn_add = ttk.Button(button_frame, text="Add file", command=add_file)
    btn_add.pack(side=LEFT, padx=5)

    btn_delete = ttk.Button(button_frame, text="Delete file", command=delete_file)
    btn_delete.pack(side=LEFT, padx=5)

    btn_save = ttk.Button(button_frame, text="Save config", command=save_file)
    btn_save.pack(side=LEFT, padx=5)

    button_frame.pack(side=BOTTOM)


root = app_init()
root.protocol("WM_DELETE_WINDOW", finish)
start()
button_init()
print(programs)
root.mainloop()
