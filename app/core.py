import numpy as np

def sample_signal(signal, t_cont, sampling_rate):
    t_sampled = np.arange(0, t_cont[-1], 1 / sampling_rate)
    sampled = np.interp(t_sampled, t_cont, signal)
    return t_sampled, sampled

def quantize_signal(sampled_signal, bits, min_val=-1, max_val=1):
    levels = 2 ** bits
    quantized = np.round((sampled_signal - min_val) / (max_val - min_val) * (levels - 1))
    quantized = (quantized / (levels - 1)) * (max_val - min_val) + min_val
    return quantized

def reconstruct_signal(t_sampled, quantized, t_cont):
    return np.interp(t_cont, t_sampled, quantized)

def calculate_quantization_error(original, reconstructed):
    return original - reconstructed

def calculate_snr(original, reconstructed):
    noise = original - reconstructed
    signal_power = np.sum(original ** 2)
    noise_power = np.sum(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)

def calculate_thd(signal):
    fft_vals = np.fft.fft(signal)
    harmonics = np.abs(fft_vals)
    fundamental = harmonics[1]  # Skip DC
    thd = np.sqrt(np.sum(harmonics[2:] ** 2)) / fundamental
    return thd * 100