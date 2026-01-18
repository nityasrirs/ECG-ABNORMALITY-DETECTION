from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def analyze_ecg(ecg_signal, fs=360):
    # SHORT SIGNAL DEMO MODE
    if len(ecg_signal) < 10:
        return "ECG Detected (Short Signal - Demo Result)"

    peaks, _ = find_peaks(ecg_signal, distance=fs * 0.6)

    if len(peaks) < 2:
        return "Abnormal ECG (No clear heartbeats)"

    rr = np.diff(peaks) / fs
    hr = int(60 / np.mean(rr))

    if hr < 60:
        return f"Bradycardia (HR: {hr} bpm)"
    elif hr > 100:
        return f"Tachycardia (HR: {hr} bpm)"
    else:
        return f"Normal ECG (HR: {hr} bpm)"

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"})

    try:
        data = pd.read_csv(file, header=None)
        ecg = data.iloc[:, 0].values
        result = analyze_ecg(ecg)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": "Invalid ECG file"})

if __name__ == "__main__":
    app.run(debug=True)
