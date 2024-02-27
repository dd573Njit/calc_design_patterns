# main.py
from app import App
from command_config import dict
if __name__ == "__main__":
    app = App(dict)
    app.start()
