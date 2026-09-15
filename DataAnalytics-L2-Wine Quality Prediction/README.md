# Wine Quality Prediction — Classification Models

Training and comparing multiple classification models to predict red wine quality from its physicochemical properties (acidity, density, alcohol content, etc.).

## 📌 Objective

- Explore the relationship between a wine's chemical properties and its quality rating
- Address a real class-imbalance problem instead of ignoring it
- Train and fairly compare 3 different classifier types
- Recommend a model for deployment based on more than just accuracy

## 📂 Dataset

- **File:** `winequality-red.csv`
- **Source:** [UCI Machine Learning Repository — Wine Quality Dataset](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Size:** 1,599 samples × 11 physicochemical features + 1 quality score
- **Features:** fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free/total sulfur dioxide, density, pH, sulphates, alcohol
- **Target:** `quality` — an integer score from 3–8, assigned by wine tasters

> **Class imbalance note:** the raw quality scores are heavily skewed — scores 5 and 6 make up 82.5% of the data, while scores 3 and 8 have only 10 and 18 samples respectively. This dataset is not naturally balanced, and that shapes every modelling decision below.

## 🛠️ Tech Stack

- Python 3
- pandas, numpy — data handling
- scikit-learn — `RandomForestClassifier`, `SGDClassifier`, `SVC`, train/test split, metrics
- matplotlib, seaborn — visualization
- Jupyter Notebook

## 📁 Project Structure

```
.
├── winequality-red.csv               # Raw dataset
├── Wine_Quality_Prediction.ipynb     # Full analysis & modelling notebook
└── README.md                         # This file
```

## 🔍 What's in the Notebook

1. **Load & Inspect** — shape, dtypes, null check, raw class distribution
2. **EDA** — distribution plots for all 11 features, full correlation heatmap
3. **Class Imbalance Discussion** — why the raw 6-class problem is unreliable to model directly
4. **Feature Engineering** — binned `quality` into a binary target (`Good` ≥ 7, `Not Good` ≤ 6), with the 3-class alternative explicitly considered and rejected, and reasoning documented
5. **Stratified Train/Test Split** — preserves the ~86/14 class ratio in both sets
6. **3 Classifiers Trained** — Random Forest, SGD (log-loss), and SVC (RBF kernel), each using `class_weight='balanced'`; features standardised for the scale-sensitive models (SGD, SVC)
7. **Evaluation** — accuracy, full classification report, and confusion matrix per model
8. **Feature Importance** — Random Forest's top predictive features
9. **Model Comparison Table** — accuracy, precision, recall, F1 side by side
10. **Conclusion** — which model to deploy, and why accuracy alone isn't the full story

## 📊 Key Results

| Model | Accuracy | Precision (Good) | Recall (Good) | F1 (Good) |
|---|---|---|---|---|
| **Random Forest** | **0.947** | **0.96** | 0.63 | **0.76** |
| SGD Classifier | 0.838 | 0.44 | 0.79 | 0.57 |
| SVC | 0.847 | 0.46 | 0.77 | 0.57 |

**Top predictive features:** alcohol, sulphates, volatile acidity — consistent with both the correlation analysis and known wine chemistry (high volatile acidity gives an unpleasant, vinegary taste).

## ✅ Conclusion

**Recommended model: Random Forest.** It has the best accuracy and F1 score, needs no feature scaling, and its feature importances are directly interpretable to a non-technical stakeholder.

That said, there's a genuine trade-off worth knowing: Random Forest is **precise but conservative** (misses ~37% of truly good wines), while SGD/SVC are **more sensitive but far less precise** (catch more good wines, but nearly half their "Good" predictions are wrong). Which model is actually "better" depends on whether false positives or false negatives are more costly in the real deployment context — this is discussed in full in the notebook's conclusion.

## ▶️ How to Run

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```
3. Launch the notebook:
   ```bash
   jupyter notebook Wine_Quality_Prediction.ipynb
   ```
4. Run all cells (`Kernel → Restart & Run All`).

## 📄 License

For educational/portfolio use.
