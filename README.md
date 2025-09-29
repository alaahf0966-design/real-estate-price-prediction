# Real Estate Price Prediction
Predicting house prices with Machine Learning using the Kaggle dataset: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

## Project Structure
real-estate-price-prediction/
├── data/                # Datasets (train.csv, test.csv, submissions, etc.)
├── notebooks/           # Jupyter notebooks (EDA, cleaning, modeling, tuning)
├── src/                 # Source code and saved models
├── figures/             # Visualizations (plots, heatmaps)
└── README.md            # Project documentation

## Steps
1. **EDA**: distributions, correlations, key relationships.
2. **Data Cleaning**: handle missing values, encode categoricals, align columns.
3. **Modeling**: Random Forest (baseline), XGBoost (improved).
4. **Submission**: generate `submission.csv` for Kaggle.

## Results
- Random Forest (baseline): `0.33593`
- XGBoost: `0.25687` *(RMSLE — lower is better)*

## Tech Stack
- Python: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost
- Jupyter Notebook
- Git & GitHub

## How to Run
git clone https://github.com/alaahf0966-design/real-estate-price-prediction.git
cd real-estate-price-prediction
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook

## Next Improvements
- Hyperparameter tuning (XGBoost/LightGBM)
- Feature engineering (e.g., TotalSF, interactions)
- Ensembles (XGBoost + RF + LightGBM)
- Simple API or web app for inference

## Acknowledgements
Dataset from Kaggle.
