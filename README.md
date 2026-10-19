# Rapido Replica: Real-Time Geospatial Streaming & ML Platform

## Overview
An end-to-end simulation of a ride-hailing operational engine modeled after Rapido. The platform simulates high-velocity geospatial telemetry, determines real-time dynamic surge multipliers using Gradient Boosting, and predicts Estimated Time of Arrival (ETA) by modeling traffic congestion and geographic variables.

## Architecture & Implementation
* **Telemetry & Ingestion (`streaming_simulator.py`):** Generates high-frequency ride requests, driver availability indicators, and geospatial zone imbalances across peak and off-peak operating windows.
* **Dynamic Surge Pricing (`surge_pricing_model.py`):** Implements an XGBoost regression model to determine real-time pricing multipliers based on local supply/demand ratios.
* **ETA Prediction (`eta_prediction_model.py`):** Trains a Random Forest regressor on one-hot encoded pickup/drop zones and temporal parameters to forecast trip duration, achieving an R² of 0.94 and MAE of ~2.98 minutes.

## Tech Stack
* **Languages:** Python
* **ML Frameworks:** Scikit-Learn, XGBoost
* **Data Processing:** Pandas, NumPy
* **Core Concepts:** Feature Engineering, Regression Modeling, Telemetry Simulation, Geospatial Encoding
