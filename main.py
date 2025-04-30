import os


STARTUP_PATH = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
print(STARTUP_PATH)