import numpy as np
from random import randrange

from util import *


class DataProcessor():
    # scale_type 0:none/1:major/2:minor

    def __init__(self, scale_name="D#m", scale_type=1):
        self.scale_type = scale_type # this should be calculated based on the scale name. (M or m)
        self.scale_name = scale_name.lower().rsplit('m',1)[0]
        self.notes = compute_scale_notes(self.scale_name, self.scale_type)
        self.unit_size=800/(max_midi_note-min_midi_note) # this should be tuned 
        

    def process_data(self, data):
        print("DATA: ", data)
        buffer = []
        for value in data:
            value = int(value)
            base_number = -1
            if value == 3:
                while base_number%2 != 0:
                    base_number = randrange(110,160)
            elif value == 4:
                while base_number%3 != 0:
                    base_number = randrange(140,190)
            
            midi_value=(int)(base_number/self.unit_size) + min_midi_note
            

            # quantize the value for minor/major scale
            if self.scale_type != 0:
                idx =(np.abs(self.notes-midi_value)).argmin()
                midi_value = self.notes[idx]
            
            print("NEW NOTE ADDED TO BUFFER: ", midi_value)
            buffer.append(midi_value)
        
        return buffer