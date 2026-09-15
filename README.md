# OASIS INFOBYTE — Data Analytics Internship

## 📈 Data Analytics

This repository contains the Data Analytics internship tasks completed as part of the **OASIS INFOBYTE SIP Internship**.

The tasks below cover exploratory data analysis, data cleaning, predictive modelling, and classification — demonstrating the full analytical workflow from raw data to actionable insight.

**Tasks completed in this repository:**

| Level | Task | Title |
|---|---|---|
| Level 1 | Task 1 | EDA on Retail Sales Data |
| Level 1 | Task 3 | Cleaning Data |
| Level 2 | Task 1 | Predicting House Prices with Linear Regression |
| Level 2 | Task 2 | Wine Quality Prediction |

---

# 📊 Level 1

## Task 1 — EDA on Retail Sales Data

### 🎯 Objective

Perform a thorough **Exploratory Data Analysis (EDA)** on a retail sales dataset to uncover patterns, customer behaviour trends, and actionable business insights.

### 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

### 🔍 Analysis Requirements

* Load the dataset and inspect:
  * Shape
  * Column data types
  * Null values
* Calculate descriptive statistics:
  * Mean
  * Median
  * Mode
  * Standard deviation
* Analyse monthly and quarterly sales trends.
* Analyse customer demographics:
  * Age groups
  * Gender distribution
* Identify the top 10 best-selling products.
* Analyse revenue by product category.
* Create a correlation heatmap.
* Create at least one additional visualization to identify a non-obvious insight.
* Add written observations after each visualization.
* Provide at least **3 actionable business recommendations** based on the findings.

### 📁 Folder

```text
DataAnalytics-L1-EDARetailSales/
```

---

## Task 3 — Cleaning Data

### 🎯 Objective

Demonstrate professional-level data-cleaning skills by transforming a deliberately messy dataset into a clean, analysis-ready dataset while documenting every decision.

### 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Jupyter Notebook

### 🔍 Data Cleaning Requirements

* Generate a data quality report containing:
  * Null values
  * Duplicate rows
  * Data type issues
  * Value-range anomalies
* Handle missing values using appropriate strategies.
* Identify and remove duplicate rows.
* Standardise inconsistent formatting.
* Convert dates into appropriate datetime formats.
* Detect outliers using:
  * IQR
  * Z-score
* Decide whether outliers should be capped, removed, or retained.
* Correct column data types.
* Create a **before vs. after** summary containing:
  * Null count
  * Duplicate count
  * Row count
  * Data-type accuracy
* Save the cleaned dataset as a new CSV file.

### 📁 Folder

```text
DataAnalytics-Task3-CleaningData/
```

---

# 📈 Level 2

## Task 1 — Predicting House Prices with Linear Regression

### 🎯 Objective

Build and evaluate a **Linear Regression** model to predict house prices based on features such as area, location, number of rooms, and age.

### 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

### 🔍 Analysis Requirements

* Load the dataset.
* Perform EDA.
* Check null values.
* Calculate descriptive statistics.
* Analyse the distribution of house prices.
* Discuss important predictive features.
* Handle missing values.
* Encode categorical variables using One-Hot Encoding.
* Create a correlation heatmap.
* Split the data into training and testing sets.
* Train a Linear Regression model.
* Evaluate using:
  * MSE
  * RMSE
  * R²
* Create actual-vs-predicted price scatter plots.
* Create a residual plot.
* Analyse model coefficients.
* Compare Linear Regression with Ridge and Lasso regression (bonus).

### 📌 Key Result

Every feature in the provided dataset correlated with `Price` at close to zero (even `Area`, normally the strongest predictor), giving an R² near zero and identical performance across Linear Regression, Ridge, and Lasso. The notebook documents this finding and interprets what it means, rather than treating a low score as a modelling failure.

### 📁 Folder

```text
DataAnalytics-L2-HousePricePrediction/
```

---

## Task 2 — Wine Quality Prediction

### 🎯 Objective

Train and compare multiple classification models to predict wine quality based on physicochemical properties such as acidity, density, and alcohol content.

### 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest
* SGD
* SVC
* Seaborn
* Matplotlib
* Jupyter Notebook

### 🔍 Analysis Requirements

* Load and inspect the Wine Quality dataset.
* Analyse the distribution of quality scores.
* Create distribution plots for chemical features.
* Create a correlation heatmap.
* Analyse class imbalance.
* Consider grouping quality scores into:
  * Binary classes
  * Three classes
* Justify the selected grouping.
* Perform a stratified train/test split.
* Train:
  * Random Forest
  * Stochastic Gradient Descent
  * Support Vector Classifier
* Evaluate each model using:
  * Accuracy
  * Classification report
  * Confusion matrix
* Create a feature-importance chart.
* Compare all models in a performance table.
* Identify the most suitable model for deployment.

### 📁 Folder

```text
DataAnalytics-L2-WineQualityPrediction/
```

---

# 🗂️ Repository Structure

```text
OIBSIP/
│
├── DataAnalytics-L1-EDARetailSales/
│   ├── dataset/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L1-CleaningData/
│   ├── dataset/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L2-HousePricePrediction/
│   ├── dataset/
│   ├── outputs/
│   └── README.md
│
└── DataAnalytics-L2-WineQualityPrediction/
    ├── dataset/
    ├── outputs/
    └── README.md
```

---

# 📊 Skills Demonstrated

* Exploratory Data Analysis
* Data Cleaning & Preprocessing
* Statistical Analysis
* Data Visualisation
* Outlier Detection (IQR, Z-score)
* Feature Engineering
* One-Hot Encoding
* Regression (Linear, Ridge, Lasso)
* Classification (Random Forest, SGD, SVC)
* Model Evaluation
* Business Insight Generation

---

# 📌 Data Analytics Workflow

```text
Data Collection
       ↓
Data Loading
       ↓
Data Inspection
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Visualisation
       ↓
Statistical / Machine Learning Analysis
       ↓
Model Evaluation
       ↓
Insights & Recommendations
       ↓
Final Conclusion
```

---

# 📈 Internship Outcome

These four tasks provide practical experience in transforming raw datasets into meaningful insights through **data cleaning, exploratory analysis, visualisation, statistical techniques, and machine learning** — demonstrating the complete analytical workflow from raw data to insights and recommendations.

---

## 👨‍💻 Author

**Vrutant Kar**

Data Analytics Intern<b>
OASIS INFOBYTE </b>SIP Internship
