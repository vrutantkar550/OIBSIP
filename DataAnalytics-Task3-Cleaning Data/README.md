# NFL Play-by-Play (2009–2016) — Data Cleaning

A professional-level data cleaning exercise: taking a large, deliberately messy real-world dataset and systematically transforming it into a clean, analysis-ready dataset — with every decision documented and justified.

## 📌 Objective

Demonstrate a full data cleaning workflow on a real dataset:
- Produce a data quality report before touching anything
- Handle missing data with a justified strategy per column type (not a blanket fix)
- Remove true duplicates without deleting legitimate records
- Standardise inconsistent formatting
- Detect outliers and decide, deliberately, whether to keep them
- Correct data types
- Prove the cleaning worked with a before/after comparison
- Save a clean, reusable output file

## 📂 Dataset

- **File:** `NFL_Play_by_Play_2009-2016__v3_.csv`
- **Source:** Play-by-play data for every NFL game, 2009–2016 seasons
- **Size:** 362,447 rows × 102 columns
- **Content:** Down/distance, field position, play description, play outcome, scoring, and advanced metrics (EPA, WPA, win probability)

> **Key insight this project relies on:** most of this dataset's "missing data" is *structural*, not a defect. A field like `PuntResult` is only ever populated on punt plays — it's correctly `NaN` on every pass or run play. Treating that the same as genuine missing data would lead to nonsensical imputation. The cleaning process explicitly separates structural NA from real, fixable data quality problems.

## 🛠️ Tech Stack

- Python 3
- pandas — cleaning, transformation, aggregation
- numpy — numeric operations, outlier logic
- matplotlib & seaborn — distribution/outlier visualization
- Jupyter Notebook — analysis environment

## 📁 Project Structure

```
.
├── Database.py                                   # Raw dataset
├── NFL_Data_Cleaning.ipynb                       # Full cleaning notebook
└── README.md                                     # This file
```

## 🔍 What's in the Notebook

1. **Data Quality Report** — nulls, dtypes, and duplicate check across all 102 columns
2. **Missing Data Handling** — five distinct, justified strategies depending on the column:
   - Row deletion for genuinely unrecoverable rows (down/team/description missing, 733 rows)
   - Forward-fill within game for the game clock and score margin (both are logically continuous)
   - Explicit `"Not Applicable"` category for fields that don't apply to a given play type (pass length/outcome on non-pass plays)
   - Deliberate retention of `NaN` for advanced metrics (EPA/WPA) rather than fabricating values
3. **Duplicate Removal** — 0 exact duplicates found; also tested a narrower composite key, found 58 look-alike rows, and confirmed via inspection they're legitimate distinct plays, not duplicates
4. **Standardisation** — found and fixed the Jacksonville Jaguars being coded inconsistently as both `JAC` and `JAX`; fixed one invalid `PassLength` value using a rule based on recorded air yards
5. **Outlier Detection (IQR)** — applied to `Yards.Gained`, `ydstogo`, `EPA`, `WPA`; decision made to retain all outliers since they represent real, rare football events (long touchdowns, big losses) rather than data errors
6. **Data Type Correction** — dates to `datetime64`, `GameID` to string (never numeric — it's an identifier), down/quarter/season to nullable `Int64`, categorical fields properly typed
7. **Before vs. After Summary** — row count, null count, duplicate count, and dtype accuracy compared side by side
8. **Save Cleaned Dataset** — final cleaned file written to CSV

## 📊 Key Cleaning Decisions & Rationale

| Issue | Decision | Why |
|---|---|---|
| Structural `NaN` (e.g. `down` on a kickoff) | Leave as `NaN` | Fabricating a value would misrepresent plays that never had one |
| Genuinely missing down/team/description (733 rows) | Drop rows | <0.2% of data; no reliable way to infer the true value |
| Missing game clock / score margin | Forward-fill within game | Both are logically unchanged during dead-ball plays |
| `JAC` vs `JAX` team codes | Standardise to `JAX` | Same team, inconsistent labeling — confirmed by same-season overlap |
| Invalid `PassLength` value (`"20"`) | Rule-based fix using `AirYards` | Air yards ≥ 15 is conventionally a "Deep" pass |
| Extreme `Yards.Gained` / `EPA` values | Retain, do not cap | Legitimate rare events (long TDs, game-swinging plays), not errors |

## ▶️ How to Run

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```
3. Launch the notebook:
   ```bash
   jupyter notebook NFL_Data_Cleaning.ipynb
   ```
4. Run all cells (`Kernel → Restart & Run All`).

> ⚠️ **Note on file size:** the raw and cleaned CSVs are large (~230MB). They may be slow to open in spreadsheet tools like Excel — pandas or a database/SQL tool is recommended instead.

## 📄 License

For educational/portfolio use.
