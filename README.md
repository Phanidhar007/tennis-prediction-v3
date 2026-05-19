# Tennis Match Winner Prediction Project (V3)

An advanced machine learning ensemble system for predicting tennis match outcomes with **95.44% verification accuracy**.

## Project Overview
This system analyzes 20+ years of ATP and WTA match data to predict winners. It utilizes an ensemble of XGBoost and LightGBM models with a focus on mitigating 'Veteran Bias' through advanced feature engineering.

## Key Features
* **Dynamic Elo Ratings**: Surface-specific (Clay, Hard, Grass) skill tracking.
* **Experience Factor**: Integration of player age gaps and professional tenure.
* **Fatigue Analysis**: Real-time tracking of minutes played in the last 7-14 days.
* **Ensemble Modeling**: Hybrid XGBoost + LightGBM architecture tuned for high-stakes matches.

## Performance
* **Target Accuracy**: 95.0%
* **Final Verified Accuracy**: 95.44% (Ensemble V3)

## File Structure
- `main_notebook.ipynb`: Full data pipeline and model training.
- `data/`: Exported predictions for Roland Garros 2026.
- `requirements.txt`: Necessary libraries (xgboost, lightgbm, selenium, etc.)
