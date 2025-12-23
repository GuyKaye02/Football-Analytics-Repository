# Expected Danger (xD) — Baseline Model

This project implements a baseline Expected Danger (xD) model following the
Soccermatics course specification, designed to quantify how likely a pass is
to eventually lead to a goal.

The model mirrors early action-value ideas behind expected threat (xT), while
remaining intentionally simple for instructional purposes.

---

## Project Structure

- `xD_baseline.ipynb`: notebook implementing the baseline xD model
- `xD_report.pdf`: final project report with methodology, results, and discussion

---

## Methodology

The model follows a two-stage probability chain:

\[
xD = P(\text{shot} \mid \text{pass}) \times P(\text{goal} \mid \text{shot, pass})
\]

### Stage 1 — Shot Probability
- Logistic regression
- Predicts the probability that a pass leads to a shot within 15 seconds
- Features:
  - Pass start and end coordinates
  - Distance to goal
  - Squared distance term to capture non-linear spatial effects

### Stage 2 — Goal Probability
- Linear regression (assignment requirement)
- Estimates the probability that a resulting shot becomes a goal
- Applied only to passes that led to a shot

---

## Player Aggregation

For each player:
- xD is summed over all passes
- Converted to per-90 values
- Compared against raw “danger passes” (passes leading to shots)

This allows separation of **pass quality** from **pass volume**.

---

## Results & Insights

- The model successfully identifies elite creators from the 2015/16 Premier League,
  including Mesut Özil, David Silva, and Cesc Fàbregas.
- xD rankings meaningfully differ from danger-pass volume, highlighting creative
  intent rather than just frequency.
- Position-level analysis shows attacking midfielders and full backs ranking highly,
  consistent with tactical expectations.

Detailed tables and visualizations are presented in the final report.

---

## Limitations

This baseline model is intentionally simple and has several limitations:

- No cross-validation; models are fit and evaluated on the same data
- Linear regression used for a probability task (course requirement)
- Extremely limited feature set with no contextual information
  (e.g. pressure, pass type, set pieces)

Despite this, the model produces intuitive probability rankings and serves as a
strong foundation for more advanced action-value models.

---

## Report

Full methodology, evaluation, and discussion of limitations and future extensions
are documented in:

📄 `xD_report.pdf`

---

## Notes

This baseline implementation was later extended into a regularized and
context-aware xD model with richer features and proper cross-validation.
