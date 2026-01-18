import numpy as np
from scipy.signal import find_peaks

def analyze_ecg(ecg_signal, fs=360):
    ecg_signal = np.array(ecg_signal)

    if len(ecg_signal) < fs:
        return "Abnormal (Insufficient ECG Data)"

    peaks, _ = find_peaks(ecg_signal, distance=fs*0.6)

    if len(peaks) < 2:
        return "Abnormal (No clear R-peaks)"

    rr = np.diff(peaks) / fs
    hr = 60 / np.mean(rr)

    if hr < 60:
        return f"Bradycardia (Heart Rate: {int(hr)} bpm)"
    elif hr > 100:
        return f"Tachycardia (Heart Rate: {int(hr)} bpm)"
    else:
        return f"Normal ECG (Heart Rate: {int(hr)} bpm)"
