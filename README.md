# ECG Abnormality Detection System

## Project Overview

The ECG Abnormality Detection System is a machine learning-based web application designed to assist in identifying normal and abnormal ECG signals. The system enables users to upload ECG-related files or datasets through a web interface, which are processed by a backend service and analyzed using a trained (or placeholder) machine learning model. The prediction result is displayed along with a confidence score.

This project demonstrates the integration of Frontend, Backend, Database, and Machine Learning components in a unified full-stack application.

---

## Objectives

- To develop a user-friendly interface for uploading ECG data  
- To integrate a machine learning model for ECG abnormality detection  
- To establish communication between frontend and backend using Flask API  
- To provide real-time prediction results to the user  
- To design a scalable and modular system architecture  

---

## System Architecture

The system follows a three-tier architecture:

### 1. Frontend (User Interface)
- Developed using HTML, CSS, and JavaScript  
- Supports both single file upload and entire folder upload  
- Displays prediction results and confidence score  

### 2. Backend (Flask API)
- Implemented using Python and Flask framework  
- Receives uploaded files from the frontend  
- Loads the trained machine learning model  
- Generates predictions and sends response back to frontend  

### 3. Machine Learning Model
- A placeholder (Dummy) model is currently used for demonstration  
- The model is saved as `ecg_model.pkl` using Joblib  
- The system is designed to allow replacement with a real trained ECG classification model in future  
## Project Folder Structure

