# Students Stress Prediction System

## Overview

The Student Stress Prediction System is a machine learning–powered Flask web application that analyzes 18 psychological, physical, and environmental factors to predict a student’s stress level (Low / Moderate / High) with 86.36% accuracy.

* This project fulfills the requirement of using Flask instead of Streamlit and delivers a professional, production-ready interface.

## Features

* Clean, modern, fully responsive Flask web interface
* Professional dark-blue corporate design
* 18 interactive sliders with real-time value display
* Instant prediction with color-coded results
* Pure Flask + HTML/CSS
* Model loaded once at server startup for fast predictions
* Zero external frontend frameworks

## Project Structure

**Stress-Predictor-Flask/**
│
├── app.py                              # Main Flask application + prediction logic
├── stress_classifier_model.pkl         # Trained CatBoost model (86.36% accuracy)
├── templates/
│   └── index.html                      # Beautiful frontend UI
└── static/
    └── style.css                       # Professional dark-blue styling

### Dataset Details

* Source: Student Stress Factors Dataset
* Total Features Used: 18
* Target: Stress Level (0 = Low, 1 = Moderate, 2 = High)

### Important Input Features (18)

* Anxiety Level (0–21)           * Self-Esteem (0–30)
* Mental Health History (0/1)    * Depression (0–27)
* Headache (0–5)                 * Blood Pressure (1–3)
* Sleep Quality (0–5)            * Breathing Problem (0–5)
* Noise Level (0–5)              * Living Conditions (0–5)
* Safety (0–5)                   * Basic Needs (0–5)
* Academic Performance (0–5)     * Study Load (0–5)
* Teacher-Student Relationship (0–5)
* Future Career Concerns (0–5)
* Social Support (0–3)           * Extracurricular Activities (0–5)

### Machine Learning Model

* Algorithm: CatBoost Classifier
* Accuracy: 86.36% (excellent for this dataset)
* Saved using joblib as stress_classifier_model.pkl

### Steps Performed

1. Data collection & preprocessing
2. Model training with CatBoost
3. Achieved 86.36% accuracy
4. Model saved using joblib
5. Flask web app development
6. Professional UI with sliders & instant prediction

### Flask Web UI

* Two-column responsive layout
* Real-time output next to each slider
* Big centered “Predict” button
* Color-coded alert boxes (Success / Warning / Danger)
* Dark-blue gradient background with white card

## Run the Application

* pip install flask joblib scikit-learn pandas catboost
**python app.py**
**Open browser**

## Installation & Requirements

* Python 3.8+
* Flask
* joblib
* scikit-learn
* pandas
* catboost
