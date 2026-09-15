# 🏠 House Price Prediction with Linear Regression

**Task 1** of the Oasis Infobyte / AICTE internship program — an end-to-end machine learning workflow that builds and evaluates a linear regression model to predict house prices from structural, categorical, and quality-based features.

## 📌 Objective

Build and evaluate a linear regression model that predicts house prices based on features such as area, location, number of rooms, and age. The project covers the complete data science workflow from raw data through model interpretation.

## 🛠️ Tech Stack

- Python
- pandas
- scikit-learn
- matplotlib
- seaborn
- Jupyter Notebook

## 📂 Repository Structure

```
├── House_Price_Prediction_LinearRegression.ipynb   # Main analysis notebook
├── House_Price_Prediction_Dataset.csv               # Dataset (2,000 rows)
└── README.md
```

## 📊 Dataset

`House_Price_Prediction_Dataset.csv` contains 2,000 records with the following columns:

| Column | Description |
|---|---|
| `Id` | Row identifier (dropped before modeling) |
| `Area` | House area in square feet |
| `Bedrooms` | Number of bedrooms |
| `Bathrooms` | Number of bathrooms |
| `Floors` | Number of floors |
| `YearBuilt` | Year the house was built |
| `Location` | Downtown / Suburban / Urban / Rural |
| `Condition` | Excellent / Good / Fair / Poor |
| `Garage` | Yes / No |
| `Price` | Target variable — house price ($) |

No missing values are present in the dataset.

## 🔍 Workflow

The notebook follows this pipeline:

1. **Load data & EDA** — shape, data types, null check, descriptive statistics, distribution of `Price`
2. **Feature selection discussion** — reasoning on which features are likely predictors, in a markdown cell
3. **Data cleaning & encoding** — one-hot encoding of `Location`, `Condition`, and `Garage`
4. **Correlation heatmap** — identify which features correlate most with `Price`
5. **Train/test split** — 80/20 split
6. **Model training** — scikit-learn `LinearRegression`
7. **Evaluation** — MSE, RMSE, and R² score
8. **Actual vs. predicted scatter plot**
9. **Residual plot** — checks that residuals are randomly distributed
10. **Coefficient analysis** — which features push price up or down, and by how much
11. **Bonus: Ridge & Lasso comparison** — regularised models benchmarked against plain Linear Regression

## 📈 Results

| Model | MSE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 7.83 × 10¹⁰ | ~$279,860 | -0.0067 |
| Ridge (α=1.0) | 7.83 × 10¹⁰ | ~$279,859 | -0.0067 |
| Lasso (α=100.0) | 7.83 × 10¹⁰ | ~$279,843 | -0.0066 |

**Key finding:** every feature in this dataset correlates with `Price` at close to zero — even `Area`, which is normally the strongest predictor of house price, shows a correlation of only 0.0015. As a result, the linear model performs no better than predicting the mean price for every house (R² ≈ 0), and Ridge/Lasso regularisation offer no meaningful improvement, since there's no real linear signal to overfit to in the first place.

This makes the project a useful illustration of **interpreting a negative result** — recognizing when a model's poor performance reflects the data rather than a modeling mistake — alongside the standard regression workflow.

## 🚀 How to Run

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. Install dependencies
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```
3. Launch the notebook
   ```bash
   jupyter notebook House_Price_Prediction_LinearRegression.ipynb
   ```
4. Run all cells from top to bottom.

## 🙏 Acknowledgements

- Task provided by **Oasis Infobyte**, in association with **AICTE**.
- Dataset format inspired by common Kaggle house-price datasets (e.g. Ames Housing, House Prices: Advanced Regression Techniques).
