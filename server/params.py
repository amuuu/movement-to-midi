from dataprocessor import *
from rtmidihandler import *


HOST = '192.168.43.26'  # Your local network IP    
PORT = 80
dp = DataProcessor(scale_name="Dm", scale_type=1) # scale_type 0:none/1:major/2:minor    
rt = RtMidi(port=5, channel=1)