import numpy as np
from scipy import signal

def generate_signal(signal_type, freq, time_array):
    if signal_type == "Sine":
        return np.sin(2 * np.pi * freq * time_array)
    elif signal_type == "Triangle":
        return signal.sawtooth(2 * np.pi * freq * time_array, width=0.5)
    elif signal_type == "Square":
        return signal.square(2 * np.pi * freq * time_array)
    else:
        raise ValueError("Invalid signal type")