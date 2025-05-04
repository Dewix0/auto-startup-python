import os

STARTUP_PATH = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
CONFIG_FILE = os.path.join(os.getenv('APPDATA'), 'pet_config.json')
print(STARTUP_PATH)
print(CONFIG_FILE)


