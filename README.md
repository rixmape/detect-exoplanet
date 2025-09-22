# Exoplanet Classification with AI

This project aims to automatically classify celestial objects as confirmed exoplanets or false positives using machine learning, leveraging publicly available data from the Kepler and TESS space missions. By applying a data-driven approach, this tool helps automate the analysis of large exoplanet survey datasets, which traditionally required manual review.

## Key Features

* **Unified Data Pipeline:** Standardizes and merges disparate datasets from the Kepler and TESS missions into a single, clean source for analysis.
* **Automated Exploratory Data Analysis (EDA):** The `describe.py` script provides an automated overview of the dataset, including:
  * Dataset size and data quality check for missing values.
  * Analysis of the target variable (`disposition`) to detect class imbalance.
  * Identification of potential predictive features by comparing class-wise means.
  * Alerts for features with high numbers of outliers or low variance.
  * Detection of high multicollinearity between numeric features.
* **Robust Machine Learning Model:** A **Random Forest Classifier** is trained to distinguish between confirmed exoplanets and false positives. The model is tuned using `GridSearchCV` to find the optimal hyperparameters.
* **Feature Engineering:** The `train_random_forest.py` script performs essential feature engineering steps, including **one-hot encoding** for categorical variables and automatic removal of highly correlated features.
* **Model Evaluation:** The trained model is evaluated using a comprehensive **classification report** and a **confusion matrix** to assess its performance on unseen data.
* **Reproducibility:** The trained model is saved to the `outputs` directory for later use, ensuring the process is reproducible without retraining.

## Project Structure

```plaintext
.
├── data/
│   ├── kepler.csv
│   ├── tess.csv
│   └── merged_data.csv
├── docs/
│   ├── challenge.md
│   ├── data_merge.md
│   └── ...
├── merge.py
├── describe.py
├── train_random_forest.py
├── README.md
└── requirements.txt
```

## Core Files Explained

### `merge.py`

This script is the **data preprocessing engine** of the project. It handles the critical task of combining two distinct datasets, one from the Kepler mission and one from TESS, into a single, cohesive file. The script performs:

* **Schema Unification**: Renames columns from both datasets to a common, standardized schema (e.g., `koi_period` and `pl_orbper` both become `orbital_period_days`).
* **Data Cleaning**: Adds a `mission` column to track the origin of each data point and consolidates different disposition labels (e.g., "CONFIRMED," "CP," and "KP" all become "CONFIRMED").
* **Imputation**: Fills in missing numerical values with the median of their respective columns to ensure the dataset is complete for model training.

### `describe.py`

This is an **automated EDA (Exploratory Data Analysis)** script. It takes the merged dataset and generates key insights about its structure and quality. Instead of manual data exploration, this script provides instant feedback on potential issues that could affect model performance. It alerts the user to:

* **Missing Data**: Informs if any values are missing, indicating a need for imputation.
* **Class Imbalance**: Flags if the target variable has a skewed distribution, suggesting that metrics like F1-score should be prioritized over accuracy.
* **Feature Insights**: Identifies features with significant mean differences between classes and features with a high number of outliers, which can be crucial for feature selection.
* **Multicollinearity**: Detects highly correlated features, which can be redundant and negatively impact certain models.

### `train_random_forest.py`

This script contains the **machine learning pipeline**. It takes the preprocessed data and trains a classification model to predict exoplanet status. The key steps within this script are:

* **Data Filtering & Mapping**: Filters the data to only include "CONFIRMED" and "FALSE POSITIVE" records and maps these labels to numerical values (1 and 0).
* **Feature Engineering**: Creates a new feature by one-hot encoding the `mission` column and automatically removes features that are highly correlated (above a 0.9 threshold) to improve model stability.
* **Model Training**: Uses `GridSearchCV` to train a **Random Forest Classifier**, which is a powerful ensemble model, and finds the best hyperparameters to optimize for the `f1_weighted` score.
* **Evaluation & Persistence**: Evaluates the best-performing model on a held-out test set and saves it as a `.joblib` file for future use without needing to retrain.

## Setup and Usage

1. **Dependencies:** Ensure you have Python installed, along with the necessary libraries. You can install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

2. **Data Preparation:** Run the `merge.py` script to combine the raw data and create the unified dataset.

    ```bash
    python merge.py
    ```

    This script will generate `data/merged_data.csv`.

3. **Data Analysis (Optional):** Run the `describe.py` script to get insights into the merged dataset.

    ```bash
    python describe.py
    ```

4. **Model Training:** Run the `train_random_forest.py` script to train and evaluate the machine learning model.

    ```bash
    python train_random_forest.py
    ```

    This script will save the final trained model as `outputs/random_forest_exoplanet_model.joblib`.
