import streamlit as st
import numpy as np
import pandas as pd
from app.signal_utils import generate_signal
from app.core import sample_signal, quantize_signal, reconstruct_signal, calculate_quantization_error, calculate_snr, calculate_thd
from app.plot_utils import plot_signals

st.set_page_config(layout="wide")
st.title("🎛️ ADC-DAC Converter Visualizer")

# Inputs
signal_type = st.selectbox("Select Signal Type", ["Sine", "Triangle", "Square"])
sampling_rate = st.slider("Sampling Rate (Hz)", 100, 5000, 1000, step=100)
bit_resolution = st.slider("Bit Resolution", 2, 12, 8)

# Signal generation
duration = 1
freq = 50
t_cont = np.linspace(0, duration, int(1e4))
analog = generate_signal(signal_type, freq, t_cont)

# Sampling, Quantization, Reconstruction
t_sampled, sampled = sample_signal(analog, t_cont, sampling_rate)
quantized = quantize_signal(sampled, bit_resolution)
reconstructed = reconstruct_signal(t_sampled, quantized, t_cont)

# Metrics
quant_error = calculate_quantization_error(analog, reconstructed)
snr = calculate_snr(analog, reconstructed)
thd = calculate_thd(reconstructed)

# Plot
fig = plot_signals(t_cont, analog, t_sampled, quantized, reconstructed)
st.pyplot(fig)

# Metrics display
st.subheader("📊 Metrics")
col1, col2 = st.columns(2)
col1.metric("SNR (dB)", f"{snr:.2f}")
col2.metric("THD (%)", f"{thd:.2f}")

# Export
if st.button("📥 Export CSV"):
    df = pd.DataFrame({
        "Time": t_cont,
        "Analog": analog,
        "Reconstructed": reconstructed,
        "Quantization Error": quant_error
    })
    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV", csv, "signal_data.csv", "text/csv")