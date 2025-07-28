import matplotlib.pyplot as plt

def plot_signals(t_cont, analog, t_sampled, quantized, reconstructed):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(t_cont, analog, label="Original Analog", alpha=0.6)
    ax.stem(t_sampled, quantized, linefmt='g-', markerfmt='go', basefmt=" ", label="Quantized Samples")
    ax.plot(t_cont, reconstructed, 'r--', label="Reconstructed (DAC)")
    ax.set_title("ADC-DAC Signal Visualization")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid(True)
    return fig