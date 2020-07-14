import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from IPython.display import Audio
from numpy.fft import fft, ifft
import os
from scipy.signal import find_peaks
import pytest

class BPMExtractor:
    def __init__(self, file_path: str) -> None:
        
        self.file_path = None
        
        if os.path.isfile(file_path): 
            self.file_path = file_path
        else:
            raise AttributeError("Invalid path")

        self.data = None
        self.Fs = None
        self.get_data()

    def get_data(self) -> None:
        Fs, data = read(self.file_path)
        self.Fs = Fs
        self.data = data[:,0]
        
    
    def produce_waveform(self) -> None:
        pass