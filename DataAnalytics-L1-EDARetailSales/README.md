# Amazon Sale Report — Exploratory Data Analysis

Exploratory Data Analysis (EDA) on an Amazon.in retail sales dataset to uncover sales patterns, customer behaviour trends, and actionable business insights.

## 📌 Objective

Perform a thorough EDA on the retail sales dataset to answer:
- How is revenue trending over time?
- Who is buying, and from where?
- Which products and categories drive the business?
- Where is revenue being lost (e.g. cancellations)?
- What should the business actually *do* about it?

## 📂 Dataset

- **File:** `Amazon_Sale_Report.csv`
- **Source:** Order-level sales data for an apparel seller on Amazon.in
- **Size:** ~128,975 rows × 24 columns
- **Time period:** 31 Mar 2022 – 29 Jun 2022 (~3 months)
- **Key fields:** Order ID, Date, Status, Fulfilment, Category, Style, SKU, Size, Qty, Amount, ship-city/state, B2B flag

> **Note:** This dataset does not include individual customer demographic fields (age, gender). Where the task called for demographic analysis, geographic distribution (state/city) and B2B vs. B2C order behaviour were used as the closest available proxies — this is called out explicitly in the notebook.

## 🛠️ Tech Stack

- Python 3
- pandas — data loading, cleaning, aggregation
- matplotlib & seaborn — visualization
- Jupyter Notebook — analysis environment

## 📁 Project Structure

```
.
├── Amazon_Sale_Report.csv        # Raw dataset
├── EDA_Amazon_Sale_Report.ipynb  # Full analysis notebook
└── README.md                     # This file
```

## 🔍 What's in the Notebook

1. **Initial Inspection** — shape, dtypes, null-value audit
2. **Descriptive Statistics** — mean, median, mode, std for numerical columns
3. **Time Series Analysis** — monthly and quarterly revenue trends
4. **Customer Demographics** — geographic (state/city) distribution, B2B vs. B2C breakdown
5. **Product Analysis** — top 10 best-selling SKUs, revenue by category
6. **Correlation Heatmap** — relationships between numerical variables
7. **Extra Insight** — order status & cancellation-rate analysis by category
8. **Conclusion** — key findings and actionable business recommendations

Every visualization is followed by a markdown cell with written observations.

## 📊 Key Findings

- **Set** and **kurta** categories drive ~65% of total revenue.
- **Maharashtra, Karnataka, and Telangana** are the top revenue-generating states.
- **B2B orders** are <1% of volume but have a ~8% higher average order value than B2C.
- **~14% of all orders are cancelled**, concentrated in the highest-revenue categories.
- Revenue dips in June relative to April/May, though the short data window limits confidence in seasonality claims.

## ✅ Business Recommendations

1. Double down on hero categories (Set, kurta) while testing ways to lift underperforming ones.
2. Investigate and reduce cancellations in top-revenue categories to recover lost sales.
3. Grow the B2B channel deliberately given its higher average order value.
4. Run targeted regional campaigns in top states and diagnose underperformance elsewhere.

## ▶️ How to Run

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```
3. Launch the notebook:
   ```bash
   jupyter notebook EDA_Amazon_Sale_Report.ipynb
   ```
4. Run all cells (`Kernel → Restart & Run All`).

## 📄 License

For educational/portfolio use.
