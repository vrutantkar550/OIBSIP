# OASIS INFOBYTE — Data Analytics Internship

## 📈 Data Analytics

This repository contains the Data Analytics internship tasks completed as part of the **OASIS INFOBYTE SIP Internship**.

The Data Analytics track focuses on exploratory data analysis, data cleaning, customer segmentation, predictive modelling, classification, fraud detection, application-market analysis, and NLP-based analytics.

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

### 📁 Suggested Folder

```text
DataAnalytics-L1-EDARetailSales/
```

---

## Task 2 — Customer Segmentation Analysis

### 🎯 Objective

Apply clustering algorithms to segment an e-commerce company's customers into distinct groups based on purchasing behaviour and support targeted marketing strategies.

### 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* K-Means
* Matplotlib
* Seaborn
* Jupyter Notebook

### 🔍 Analysis Requirements

* Load and inspect the dataset.
* Handle missing and inconsistent data.
* Calculate:

  * Average purchase value
  * Purchase frequency
  * Customer lifetime value
* Select 2–3 behavioural features for clustering.
* Use **RFM analysis** where appropriate:

  * Recency
  * Frequency
  * Monetary
* Standardise the data using `StandardScaler`.
* Apply **K-Means clustering**.
* Use the **Elbow Method** to determine the optimal number of clusters.
* Visualise clusters using scatter plots.
* Profile each customer segment.
* Create a bar chart showing the number of customers in each cluster.
* Recommend appropriate marketing actions for each customer segment.

### 📁 Suggested Folder

```text
DataAnalytics-L1-CustomerSegmentation/
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

### 📁 Suggested Folder

```text
DataAnalytics-L1-CleaningData/
```

---

## Task 4 — Sentiment Analysis

### 🎯 Objective

Build a machine-learning model that classifies text into **positive, negative, or neutral** sentiment to provide insights into public opinion or customer feedback.

### 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* NLTK or TextBlob
* Matplotlib
* Seaborn
* Jupyter Notebook

### 🔍 Analysis Requirements

* Load the dataset.
* Analyse the distribution of positive, negative, and neutral classes.
* Perform text preprocessing:

  * Lowercasing
  * Punctuation removal
  * Stopword removal
  * Tokenisation
  * Optional stemming/lemmatisation
* Extract features using **TF-IDF**.
* Split the dataset into training and testing sets using an 80/20 split.
* Train at least two classifiers.
* Evaluate models using:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * Confusion matrix
* Create sentiment-distribution visualisations.
* Create WordClouds for sentiment classes.
* Perform error analysis on misclassified examples.
* Identify the best-performing model.
* Discuss a possible real-world application.

### 📁 Suggested Folder

```text
DataAnalytics-L1-SentimentAnalysis/
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
* Optionally compare Linear Regression with Ridge or Lasso regression.

### 📁 Suggested Folder

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

### 📁 Suggested Folder

```text
DataAnalytics-L2-WineQualityPrediction/
```

---

## Task 3 — Fraud Detection

### 🎯 Objective

Build a machine-learning pipeline to detect fraudulent financial transactions while addressing the challenge of a heavily imbalanced dataset.

### 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Imbalanced-learn
* SMOTE
* Matplotlib
* Seaborn
* Jupyter Notebook

### 🔍 Analysis Requirements

* Load and analyse the transaction dataset.
* Determine the percentage of fraudulent transactions.
* Perform EDA on transaction amounts.
* Analyse fraud according to time of day.
* Explain why accuracy alone is misleading for highly imbalanced datasets.
* Handle class imbalance using:

  * SMOTE
  * Undersampling
  * `class_weight='balanced'`
* Use stratified train/test splitting.
* Train at least two models:

  * Logistic Regression
  * Decision Tree / Random Forest / XGBoost
* Evaluate using:

  * Precision
  * Recall
  * F1-score
  * AUC-ROC
* Analyse the Precision–Recall trade-off.
* Perform feature-importance or coefficient analysis.
* Discuss how the solution could scale to large transaction volumes.

### 📁 Suggested Folder

```text
DataAnalytics-L2-FraudDetection/
```

---

## Task 4 — Unveiling the Android App Market

### 🎯 Objective

Perform comprehensive data analysis of the **Google Play Store ecosystem**, including data cleaning, category analysis, ratings, pricing, installs, and sentiment analysis of user reviews.

### 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* TextBlob or VADER
* Jupyter Notebook
* Plotly — optional but recommended

### 🔍 Analysis Requirements

* Load the Play Store apps dataset.
* Load the user reviews dataset.
* Correct incorrect data types.
* Handle missing values.
* Remove duplicates.
* Analyse app categories.
* Identify highly saturated categories.
* Analyse rating distributions.
* Calculate average ratings by category.
* Analyse app size versus number of installs.
* Analyse:

  * Free vs. paid applications
  * Paid-app prices
  * Estimated revenue by category
* Perform sentiment analysis on user reviews.
* Classify reviews as:

  * Positive
  * Negative
  * Neutral
* Analyse sentiment by app category.
* Create at least one interactive visualisation using Plotly where possible.
* Provide 3 data-driven insights for someone planning to launch a new application.

### 📁 Suggested Folder

```text
DataAnalytics-L2-GooglePlayStoreAnalysis/
```

---

## Task 5 — Autocomplete and Autocorrect Data Analytics

### 🎯 Objective

Analyse the efficiency and accuracy of autocomplete and autocorrect algorithms using NLP techniques and compare different approaches for text prediction and spelling correction.

### 🛠️ Tech Stack

* Python
* Pandas
* NLTK
* PySpellChecker or TextDistance
* Collections
* Matplotlib
* Jupyter Notebook

### 🔍 Analysis Requirements

* Collect or download a large text corpus.
* Perform NLP preprocessing:

  * Tokenisation
  * Lowercasing
  * Punctuation removal
  * Stopword removal
* Implement an autocomplete system using a frequency-based:

  * Bigram model
  * Trigram model
* Test autocomplete using at least 10 input prefixes.
* Display the top 3 predictions for each prefix.
* Implement autocorrect using edit-distance-based correction.
* Test autocorrect using at least 20 deliberately misspelled words.
* Measure correction accuracy.
* Calculate precision and recall.
* Compare at least two approaches.
* Visualise the 20 most frequent words.
* Create a confusion matrix for autocorrect.
* Discuss limitations compared with production systems such as Google Keyboard.

### 📁 Suggested Folder

```text
DataAnalytics-L2-AutocompleteAutocorrect/
```

---

# 🗂️ Repository Structure

```text
OIBSIP/
│
├── DataAnalytics-L1-EDARetailSales/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L1-CustomerSegmentation/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L1-CleaningData/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L1-SentimentAnalysis/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L2-HousePricePrediction/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L2-WineQualityPrediction/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L2-FraudDetection/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
├── DataAnalytics-L2-GooglePlayStoreAnalysis/
│   ├── dataset/
│   ├── notebook/
│   ├── outputs/
│   └── README.md
│
└── DataAnalytics-L2-AutocompleteAutocorrect/
    ├── dataset/
    ├── notebook/
    ├── outputs/
    └── README.md
```

---

# 📊 Skills Demonstrated

Through these Data Analytics tasks, the internship work covers:

* Exploratory Data Analysis
* Data Cleaning
* Data Preprocessing
* Statistical Analysis
* Data Visualisation
* Time-Series Analysis
* Customer Segmentation
* RFM Analysis
* K-Means Clustering
* Regression
* Classification
* Model Evaluation
* Imbalanced Data Analysis
* Fraud Detection
* Sentiment Analysis
* Natural Language Processing
* TF-IDF
* Autocomplete
* Autocorrect
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

The Data Analytics internship tasks provide practical experience in transforming raw datasets into meaningful insights through **data cleaning, exploratory analysis, visualisation, statistical techniques, machine learning, and NLP-based analytics**.

The projects are designed to demonstrate the complete analytical workflow from **raw data to insights and recommendations**.

---

## 👨‍💻 Author

**Vrutant Kar**

Data Analytics Intern
OASIS INFOBYTE SIP Internship

---
