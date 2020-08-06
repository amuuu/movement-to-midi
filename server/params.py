from dataprocessor import *
from rtmidihandler import *


HOST = '192.168.43.26'  # Your local network IP    
PORT = 80

dp = DataProcessor(scale_name="Dm", scale_type=1) # scale_type:
                                                  # 0: none
                                                  # 1: major
                                                  # 2: minor
                                                  # to be fixed: scale_type doesn't work at the moment.
                                                  # you should specify minor and major in the scale_name

rt = RtMidi(port=2, channel=1) # the port which you want
                               # to send the midiout signal to.
                               # (the port number starts from 0)

delay_time = 0.2 # the time which the server
                 # waits before playing the next note
                 # (sending the next midiout signal)