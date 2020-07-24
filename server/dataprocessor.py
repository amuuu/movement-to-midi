import numpy as np

from util import *


class DataProcessor():
    # scale_type 0:none/1:major/2:minor

    def __init__(self, scale_name="D#m", scale_type=1):
        self.scale_type = scale_type # this should be calculated based on the scale name. (M or m)
        self.scale_name = scale_name.lower().rsplit('m',1)[0]
        self.notes = compute_scale_notes(self.scale_name, self.scale_type)
        self.unit_size=800/(max_midi_note-min_midi_note) # this should be tuned 
        

    def process_data(self, data):
        buffer = []
        for value in data:
            midi_value=(int)(data/self.unit_size) + min_midi_note
            
            # quantize the value for minor/major scale
            if self.scale_type != 0:
                idx = (np.abs(self.notes-value)).argmin()
                midi_value = self.notes[idx]
            
            buffer.append(midi_value)
        
        return buffer