
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_loader import load_eeg_data, basic_sanity_check
from src.preprocessing import handle_missing_values, remove_outliers_iqr, scale_features
from src.feature_engineering import add_statistical_features, add_channel_difference_features
from src.visualize import (
    plot_class_distribution,
    plot_feature_distributions,
    plot_correlation_heatmap,
    plot_confusion_matrix,
    plot_roc_curve,
    plot_feature_importance,
)
from src.train import train_logistic_regression, train_random_forest, train_svm
from src.evaluate import evaluate_model, save_classification_report, build_comparison_table


RAW_DATA_PATH = os.path.join("dataset", "raw", "eeg_eye_state.csv")
PROCESSED_DATA_PATH = os.path.join("dataset", "processed", "eeg_processed.csv")
LABEL_COLUMN = "eye_state"
EEG_CHANNELS = [
    "AF3", "F7", "F3", "FC5", "T7", "P7", "O1",
    "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"
]


def main():
    """Run the full BrainWave AI EEG classification pipeline end-to-end."""

    print("\nSTEP 1: Loading data...")
    df = load_eeg_data(RAW_DATA_PATH)
    basic_sanity_check(df)

    print("\nSTEP 2: Generating exploratory plots...")
    plot_class_distribution(df, LABEL_COLUMN, "images/eda/class_distribution.png")
    plot_feature_distributions(df, EEG_CHANNELS, "images/eda/feature_distributions.png")
    plot_correlation_heatmap(df, "images/eda/correlation_heatmap.png")

    print("\nSTEP 3: Preprocessing...")
    df = handle_missing_values(df)
    df = remove_outliers_iqr(df, EEG_CHANNELS, label_column=LABEL_COLUMN)

   
    print("\nSTEP 4: Engineering new features...")
    df = add_statistical_features(df, EEG_CHANNELS)
    df = add_channel_difference_features(df)

   
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Saved processed dataset to {PROCESSED_DATA_PATH}")


    print("\nSTEP 5: Splitting into train/test sets...")
    X = df.drop(columns=[LABEL_COLUMN])
    y = df[LABEL_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Training samples: {len(X_train)} | Test samples: {len(X_test)}")

  
    print("\nSTEP 6: Scaling features...")
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)

    
    print("\nSTEP 7: Training models (this may take a few minutes)...")
    log_reg_model = train_logistic_regression(X_train_scaled, y_train)
    rf_model = train_random_forest(X_train_scaled, y_train)
    svm_model = train_svm(X_train_scaled, y_train)

    models = {
        "Logistic Regression": log_reg_model,
        "Random Forest": rf_model,
        "SVM": svm_model,
    }

 
    print("\nSTEP 8: Evaluating models...")
    all_results = []
    for name, model in models.items():
        result = evaluate_model(model, X_test_scaled, y_test, name)
        all_results.append(result)

        save_classification_report(result["report_text"], name, "results/classification_reports")

        plot_confusion_matrix(
            y_test, result["y_pred"], name,
            f"images/confusion_matrices/{name.replace(' ', '_').lower()}_cm.png"
        )

   
        y_proba = model.predict_proba(X_test_scaled)[:, 1]
        plot_roc_curve(
            y_test, y_proba, name,
            f"images/roc_curves/{name.replace(' ', '_').lower()}_roc.png"
        )

    
    plot_feature_importance(
        X.columns, rf_model.feature_importances_, "Random Forest",
        "images/eda/random_forest_feature_importance.png"
    )

    
    print("\nSTEP 9: Comparing all models...")
    comparison_df = build_comparison_table(all_results, "results/metrics_comparison.csv")
    best_model_name = comparison_df.iloc[0]["Model"]
    best_model = models[best_model_name]
    print(f"\nBest performing model: {best_model_name}")

   
    print("\nSTEP 10: Saving best model and scaler...")
    os.makedirs("models", exist_ok=True)
    joblib.dump(best_model, "models/best_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    print("Saved: models/best_model.pkl and models/scaler.pkl")

    print("\nPipeline complete! Check the results/ and images/ folders for outputs.")


if __name__ == "__main__":
    main()
