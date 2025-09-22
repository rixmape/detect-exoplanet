import pandas as pd
import numpy as np

df = pd.read_csv("data/merged_data.csv")
rows, cols = df.shape

print("--- 📊 DATASET OVERVIEW ---")
print(f"Loaded dataset with {rows} observations and {cols} features.")

missing_values = df.isnull().sum().sum()
if missing_values == 0:
    print("✅ Data Cleanliness: No missing values found in the dataset.")
else:
    print(f"❗️ Data Quality Alert: Found {missing_values} total missing values. Imputation may be incomplete.")

print("\n--- 🎯 TARGET VARIABLE ANALYSIS (disposition) ---")
disposition_dist = df["disposition"].value_counts(normalize=True) * 100
dist_str = ", ".join([f"{k}: {v:.1f}%" for k, v in disposition_dist.items()])
print(f"Distribution: {dist_str}")

if "FALSE POSITIVE" in disposition_dist.index and disposition_dist["FALSE POSITIVE"] > 40:
    print("❗️ Insight: Dataset is imbalanced towards 'FALSE POSITIVE'. Prioritize F1-score over accuracy for model evaluation.")

print("\n--- 🔬 AUTOMATED FEATURE INSIGHTS ---")
target_col = "disposition"
exclude_cols = ["star_id", "object_name", target_col, "alias"]
numeric_cols = df.select_dtypes(include=np.number).columns.drop(exclude_cols, errors="ignore")

for col in numeric_cols:
    grouped_means = df.groupby(target_col)[col].mean()
    mean_confirmed = grouped_means.get("CONFIRMED")
    mean_fp = grouped_means.get("FALSE POSITIVE")

    if mean_confirmed is not None and mean_fp is not None and mean_confirmed > 0:
        ratio = mean_fp / mean_confirmed
        if ratio > 1.5 or ratio < 0.67:
            print(f"❗️ Potential Predictor: '{col}' shows a significant mean difference between classes (CONFIRMED: {mean_confirmed:.2f}, FALSE POSITIVE: {mean_fp:.2f}).")

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    if IQR > 0:
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_percentage = len(outliers) / rows * 100
        if outlier_percentage > 2:
            print(f"❗️ Outlier Alert: '{col}' has a high percentage of potential outliers ({outlier_percentage:.1f}%). Consider scaling or transformation.")

categorical_cols = df.select_dtypes(include=["object", "category"]).columns.drop(exclude_cols, errors="ignore")

for col in categorical_cols:
    num_unique = df[col].nunique()
    if num_unique == 1:
        print(f"❗️ Low Variance: Categorical feature '{col}' has only one unique value. It should be removed.")
    if num_unique > rows * 0.5:
        print(f"❗️ High Cardinality: Categorical feature '{col}' has {num_unique} unique values. It may be an identifier or require special encoding.")

print("\n--- ⛓️ MULTICOLLINEARITY ANALYSIS ---")
numeric_df = df.select_dtypes(include=np.number)
corr_matrix = numeric_df.corr().abs()
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
top_corr = upper_tri.stack().sort_values(ascending=False)

if not top_corr.empty and top_corr.iloc[0] > 0.8:
    f1, f2 = top_corr.index[0]
    corr_val = top_corr.iloc[0]
    print(f"❗️ High multicollinearity found. '{f1}' and '{f2}' are highly correlated ({corr_val:.2f}). Consider removing one.")
else:
    print("✅ No strong multicollinearity detected between numeric features (threshold > 0.8).")
