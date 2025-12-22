# Expected Goals (xG) Model — Event-Level Football Data

## Overview
This project develops probabilistic expected goals (xG) models using event-level football data, with a focus on rigorous binary classification, out-of-sample evaluation, and probability calibration.

The primary goal was to compare multiple modeling approaches for estimating shot-to-goal probability and to evaluate them using metrics appropriate for probabilistic predictions.

> **Note:** This project was developed as part of a group project.  
> I led the problem formulation, data sourcing, and modeling framework, including the binary classification setup, cross-validation strategy, and out-of-sample evaluation.  
> The Streamlit application was primarily implemented by a collaborator.  
> Original collaborative repository:  
> https://github.com/kaspar-soukup/expected_goals

---

## Project Structure

- `notebooks/`: data collection, exploratory analysis, feature engineering, and model training notebooks
- `report/`: final project report containing model comparison and evaluation results
- `app/`: Streamlit application for interactive xG visualization

---

## Data
- Event-level football data  
- 45,000+ shots  
- Shot-level spatial and contextual features (angle, distance, under pressure, goalkeeper positioning etc.)

---

## Modeling Framework

The xG task was formulated as a **binary classification problem**:

- Target variable: binary shot outcome (1 = goal, 0 = no goal)

- Models estimate the probability of a goal given shot-level features

The following model classes were implemented and compared:
- Logistic Regression (L1 / Lasso)
- Random Forest
- Gradient Boosted Trees
- Neural Network (TensorFlow)

---

## Evaluation & Validation
Model performance was assessed using **out-of-sample evaluation**:

- Cross-validation for robust generalization
- ROC-AUC to assess ranking ability
- Brier score and reliability curves to assess probability calibration

This evaluation framework emphasized not only predictive power, but also the quality and interpretability of predicted probabilities.

---

## Deployment
- Interactive Streamlit application enabling real-time manipulation of shot features
- Visualization of model-predicted xG values across different scenarios

The Streamlit app was developed collaboratively and serves as a visualization and exploration tool rather than a production deployment.

---

## My Contributions
- Defined the expected goals problem as a binary classification task
- Designed the train/test and cross-validation strategy
- Implemented and compared multiple xG model classes
- Led model evaluation using ROC-AUC, Brier score, and calibration curves
- Interpreted out-of-sample results and model trade-offs
- Integrated modeling outputs into the final project deliverables

---

## Notes
While developed collaboratively, this project reflects my approach to probabilistic modeling, model validation, and performance evaluation in football analytics.
