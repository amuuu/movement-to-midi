import rtmidi
import time

from signalthread import *


class RtMidi():
    def __init__(self, port, channel):
        self.port = port
        self.channel = channel

        self.midiout = rtmidi.MidiOut()
        self.available_ports = self.midiout.get_ports()

        self.buffer = []
        
        self.last_tick = time.time()

        print(self.available_ports)
        if self.available_ports:
            self.midiout.open_port(self.port)
        else:
            self.midiout.open_virtual_port("Virtual output")

    def send_signal(self):
        current_time = time.time()
        if current_time-self.last_tick > 5:
            self.last_tick = current_time
            self.buffer.reverse()
            #print(self.buffer.pop())
            note = self.buffer.pop()
            play_thread = midi_signal_thread(self.midiout, note)
            print("Playing", note)
            self.buffer.reverse()        
            play_thread.start()
