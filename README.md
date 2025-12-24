# Football Analytics Portfolio

This repository contains selected football analytics projects focused on
probabilistic modeling, football data analysis (event & tracking), and player/action valuation.

Primary tools: Python, scikit-learn, TensorFlow, event & tracking data, R

---

## 📌 Projects

### ⚽ Expected Goals (xG) Model — Event-Level Football Data
**Python | scikit-learn | TensorFlow | Probabilistic Modeling | Calibration | Streamlit**

Built probabilistic expected goals (xG) models on 45,000+ shots using event-level football data.

- Models: Logistic Regression (L1/Lasso), Random Forests, Gradient Boosted Trees, Neural Network (TensorFlow)
- Evaluation: ROC-AUC and probability calibration (reliability curves)
- Deployment: Interactive Streamlit app for real-time manipulation of shot features and visualization of model-predicted xG

➡️ [View project](projects/Expected_Goals_Model)

---

## 📊 Event-Level Action Valuation (xD)

### ⚽ Expected Danger (xD) Model — Regularized Logistic Framework
**Python | scikit-learn | L1 Logistic Regression | Cross-Validation**

Built an Expected Danger (xD) model estimating how much each pass increases the probability of scoring within the next 15 seconds.

- Probability chain: P(goal | pass) = P(shot within 15s | pass) × P(goal | shot)
- L1-regularized logistic regression at both stages
- Rich contextual features (pass type, height, set play, pressure)
- 5-fold cross-validation, ROC-AUC ≈ 0.80

➡️ [View project](projects/expected_danger/regularized)

#### Baseline xD Model (Soccermatics specification)
Implemented an initial xD baseline to emphasize probability chaining and spatial feature engineering.

- Logistic regression for shot probability
- Linear regression for shot-to-goal conversion (course specification)

➡️ [View baseline](projects/expected_danger/baseline)

---

## 🧠 Player & Market Analysis

### 🎯 Player Scouting Analysis — Fabián Ruiz (Euro 2024)
**Python | StatsBomb Open Data | mplsoccer | Visualization**

Conducted a data-driven scouting analysis of Fabián Ruiz using Euro 2024 event data.

- Passing quality, press resistance, ball progression, chance creation
- Custom visualizations: pass maps, pressure-adjusted charts, event density plots
- Peer benchmarking against central/defensive midfielders

➡️ [View project](projects/scouting_reports/fabian_ruiz_euro2024)

---

### 📊 Transfer Market Valuation — Positional Analysis
**R | WorldFootballR | Transfermarkt | FBref**

Analyzed 6 seasons of European transfer data (3,000+ transfers) across the Big 5 leagues to quantify positional market valuations.

- Categorized players into 10 tactical positions
- Identified market premiums, undervalued roles, and cross-league inefficiencies
- Highlighted trends such as rising premiums for left-footed CBs and ball-playing GKs

➡️ [View project](projects/transfer_market_analysis)

---
Also includes qualitative football analysis combining video, telestration, and descriptive data to support player and tactical evaluation
---

## 📬 Contact
- GitHub: https://github.com/GuyKaye02
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/guykaye/)

