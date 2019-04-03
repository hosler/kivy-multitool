from mt_api import app as flaskapp
from mt_gui import MultiToolApp
import threading

if __name__ == '__main__':
    flaskapp.use_reloader = False
    fl = threading.Thread(target=flaskapp.run, kwargs={'host': "0.0.0.0"})
    fl.daemon = True
    fl.start()
    MultiToolApp().run()