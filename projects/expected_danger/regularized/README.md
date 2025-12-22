# Expected Danger (xD) — Regularized Logistic Framework

Built a pass-level Expected Danger (xD) model using an explicit probability chain:

P(goal | pass) = P(shot within 15s | pass) × P(goal | shot)

- L1-regularized logistic regression at both stages
- Rich contextual features (pass type, height, set play, pressure)
- 5-fold cross-validation
- ROC-AUC ≈ 0.80

The full pipeline is implemented in a single notebook with clearly labeled sections.
