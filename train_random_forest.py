import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def prepare_data(df):
    df = df[df["disposition"].isin(["CONFIRMED", "FALSE POSITIVE"])]
    df["disposition"] = df["disposition"].map({"CONFIRMED": 1, "FALSE POSITIVE": 0})
    return df


def engineer_features(df):
    features_to_drop = ["rowid", "star_id", "object_name", "alias", "disposition"]
    features = df.drop(columns=features_to_drop, errors="ignore")
    target = df["disposition"]

    features = pd.get_dummies(features, columns=["mission"], drop_first=True)

    corr_matrix = features.corr().abs()
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.9)]
    features = features.drop(columns=to_drop)

    print(f"Removed {len(to_drop)} highly correlated features: {to_drop}")

    return features, target


def train_and_evaluate_model(X_train, y_train, X_test, y_test):
    model = RandomForestClassifier(
        random_state=42,
        class_weight="balanced",
        n_jobs=-1,
    )

    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [10, 20, None],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
        "max_features": ["sqrt", "log2"],
    }

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=5,
        scoring="f1_weighted",
        verbose=1,
        n_jobs=-1,
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_
    print("\nBest Hyperparameters Found:")
    print(grid_search.best_params_)

    y_pred = best_model.predict(X_test)

    print("\n--- Model Evaluation on Test Set ---")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    return best_model


def show_feature_importance(model, feature_names):
    importances = model.feature_importances_
    feature_importance_df = pd.DataFrame({"feature": feature_names, "importance": importances})
    feature_importance_df = feature_importance_df.sort_values(by="importance", ascending=False)

    print("\n--- Top 15 Most Important Features ---")
    print(feature_importance_df.head(15))


def main():
    df = pd.read_csv("data/merged_data.csv")

    df_prepared = prepare_data(df)
    X, y = engineer_features(df_prepared)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print(f"\nTraining model on {len(X_train)} samples and testing on {len(X_test)} samples.")

    final_model = train_and_evaluate_model(X_train, y_train, X_test, y_test)
    show_feature_importance(final_model, X.columns)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    model_path = os.path.join(output_dir, "random_forest_exoplanet_model.joblib")
    joblib.dump(final_model, model_path)
    print(f"\n✅ Final model saved to '{model_path}'")


if __name__ == "__main__":
    main()
