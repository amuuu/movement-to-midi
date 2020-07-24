import threading
import multiprocessing 
import time
import rtmidi

from rtmidihandler import *
from init import *

class main_play_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def run(self):
        while True:
            try:
                if len(rt.buffer) != 0:
                    rt.send_signal() # pops a note from the rtmidi buffer and plays it
                    time.sleep(0.3)
            finally:
                pass