import socket
from dataprocessor import *
from rtmidihandler import *

HOST = '192.168.43.26'  # Your local network IP
PORT = 80

print("Initializing the server on", HOST, ":", PORT)
dp = DataProcessor(scale_name="D#m", scale_type=1) # scale_type 0:none/1:major/2:minor
rt = RtMidi(port=2, channel=1)
print("Server is up and listening...")

with rt.midiout:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            try:
            # with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        print(data)
                        
                        raw_data = data.decode("utf-8")
                        if "TCP" not in raw_data:
                            string_buffer = raw_data.split('-')
                            rt.buffer.extend(dp.process_data(string_buffer))
        
            
                    rt.send_signal() # pops a note from the rtmidi buffer and plays it

            finally:
                conn.close()


rt.midiout.close_port()
del rt.midiout