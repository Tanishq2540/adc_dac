# ADC-DAC Converter Visualizer

An interactive Python application that visualizes the process of Analog-to-Digital (ADC) and Digital-to-Analog (DAC) conversion. Built using **Streamlit** (Web GUI) and **Tkinter** (Desktop GUI), this tool allows real-time signal manipulation and analysis.

---

## 🔧 Features

- **Adjustable Parameters**: 
  - Sampling Rate (slider)
  - Bit Resolution (slider)
  - Signal Type (Sine, Square, Triangle)

- **Real-time Metrics**:
  - Quantization Error
  - Signal-to-Noise Ratio (SNR)
  - Total Harmonic Distortion (THD)

- **Export Capabilities**:
  - Save plots and quantized data as `.csv`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/adc-dac-visualizer.git
cd adc-dac-visualizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Activate it:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Web App

```bash
streamlit run app/app.py
```

---

## 📁 Project Structure

```text
adc-dac-visualizer/
├── app/
│   ├── app.py
│   ├── gui_utils.py
│   ├── signal_utils.py
│   ├── metrics_utils.py
│   ├── plot_utils.py
├── data/
│   └── output.csv
├── requirements.txt
├── .gitignore
├── README.md
```

---

## 📃 License

MIT License. Feel free to fork and modify.