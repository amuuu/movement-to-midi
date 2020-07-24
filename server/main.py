import socket

from dataprocessor import *
from rtmidihandler import *
from mainplaythread import *
from params import *

main_playing_thread = main_play_thread()
print("Initialized the server on", HOST, ":", PORT)
print("Server is up and listening...")

with rt.midiout:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        main_playing_thread.start()

        while True:
            conn, addr = s.accept()
            
            try:
            # with conn:
                print('Connected by', addr)
                while True:    
                    # recieve new data.
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        print(data)
                        
                        raw_data = data.decode("utf-8")
                        if "TCP" not in raw_data:
                            string_buffer = raw_data.split('-')
                            rt.buffer.extend(dp.process_data(string_buffer))

            finally:
                conn.close()
                


rt.midiout.close_port()
del rt.midiout