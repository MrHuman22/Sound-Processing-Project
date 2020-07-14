from BPMExtractor import BPMExtractor
import pytest
import os
import numpy as np

valid_file_path = "C:\\Users\\pwn394\\Documents\\Code\\Sound-Processing-Project\\Sound_Tests\\human-heartbeat-60-bpm.wav"

def test_BPMExtractor_init_throws_error_on_invalid_file_path():
    invalid_file_path = "213181__fenrirfangs__human-heartbeat-60-bpm.wav"
    with pytest.raises(AttributeError): 
        BPMExtractor(invalid_file_path)    

def test_BPMExtractor_successfully_init_on_valid_file_path():
    bpmextractor = BPMExtractor(valid_file_path)
    assert bpmextractor.file_path == valid_file_path

def test_BPMExtractor_get_data_correct_Fs():
    bpmextractor = BPMExtractor(valid_file_path)
    assert bpmextractor.Fs == 44100

def test_BPMExtractor_get_data_successfully_extracts_data():
    bpmextractor = BPMExtractor(valid_file_path)
    assert type(bpmextractor.data) == np.ndarray