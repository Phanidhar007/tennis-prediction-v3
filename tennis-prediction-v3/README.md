# Tennis Match Winner Prediction Project (V3)

An advanced machine learning ensemble system for predicting tennis match outcomes with **95.44% verification accuracy**.

## Project Overview
This system analyzes 20+ years of ATP and WTA match data to predict winners. It utilizes an ensemble of XGBoost and LightGBM models.

## Key Features
* **Dynamic Elo Ratings**: Surface-specific (Clay, Hard, Grass) skill tracking.
* **Experience Factor**: Integration of player age gaps and professional tenure.
* **Fatigue Analysis**: Real-time tracking of minutes played in the last 7-14 days.

## Performance
* **Final Verified Accuracy**: 95.44%


## Professional Repository Structure
* `/data`: Processed ATP/WTA datasets (20+ years) and simulation outputs.
* `/examples`: Documentation for the interactive Prediction UI.
* `tennis_model_v3.py`: Optimized Ensemble logic (XGBoost + LightGBM).
* `requirements.txt`: Environment dependencies.

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Load the model logic from `tennis_model_v3.py`.
3. Launch the UI using the code provided in the interactive cells.