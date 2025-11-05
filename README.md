# Football-Analytics-Repository
This GitHub repository is designed to share my work in football analytics

**📊 Most Valuable Position Analysis — R (Summer 2023)**

Scraped & unified 6 seasons of European transfer-market data (3,000+ transfers) across the top 5 leagues using WorldFootballR from Transfermarkt and FBref; categorized players into 10 tactical positions.

Quantified positional value trends by analyzing transfer fees, market valuations, and player characteristics to identify premium positions, undervalued roles, and cross-league pricing inefficiencies.

Discovered market shifts such as rising premiums for left-footed center-backs & ball-playing goalkeepers, and trend toward shorter-distance GK distribution — providing data-driven positional arbitrage insights for recruitment strategies.


**🎯 Player Scouting Analysis — Fabián Ruiz, Euro 2024**

Python | StatsBomb Open Data | mplsoccer | Soccermatics Project 1 

Conducted a data-driven scouting report on Spain midfielder Fabián Ruiz, using open-source StatsBomb Euro 2024 event data to evaluate his passing quality, press-resistance, ball progression and involvement in chance creation.

Built custom visualizations with mplsoccer and matplotlib — including pass maps, pressure-adjusted passing charts, event-density plots, and quadrant comparisons to communicate playing style and efficiency.

Benchmarked against positional peers (central/defensive midfielders) to contextualize his performance profile, highlighting Ruiz’s standout passing security under pressure, forward progression, and link play within Spain’s possession-first structure.


**⚽ Expected Danger (xD) Model — Premier League 2015/16**

Python | Scikit-learn | Event Data Modeling | Logistic & Linear Regression 

Constructed an Expected Danger (xD) model using Premier League 2015/16 event data, identifying passes that lead to shots within 15 seconds and applying the chain rule to estimate goal contribution:

P(goal within 15s∣pass)= P(shot within 15s∣pass)×P(goal within 15s∣pass leads to shot)


Developed two machine-learning models in Python (Scikit-learn):
• Logistic regression to predict shot probability from pass location features
• Linear regression to model shot-to-goal conversion likelihood
Used engineered spatial inputs: pitch-coordinate transforms, distances, and nonlinear terms to capture attacking threat.


Validated results via football intelligence — elite playmakers such as Mesut Özil, Santi Cazorla, and Cesc Fàbregas emerged as top performers, matching tactical expectations from the 2015/16 season.

“Why linear regression instead of logistic for goals?”

Answer:

This followed the Soccermatics course spec. A logistic model is standard in industry; here the focus was understanding the probability chain and feature engineering rather than optimizing model class.
