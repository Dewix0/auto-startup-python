import os
from app_gui import root

STARTUP_PATH = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
print(STARTUP_PATH)


#Запуск приложения
root.mainloop()