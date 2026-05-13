from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
DATA_PATH = DATA_DIR / "winequality-red.csv"
UCI_DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
RANDOM_STATE = 42


def ensure_directories() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def download_dataset_if_needed() -> None:
    if DATA_PATH.exists():
        return

    print("data/winequality-red.csv not found. Downloading public UCI copy of the same dataset...")
    response = requests.get(UCI_DATA_URL, timeout=30)
    response.raise_for_status()
    DATA_PATH.write_bytes(response.content)
    print(f"Saved dataset to {DATA_PATH}")


def load_data() -> pd.DataFrame:
    download_dataset_if_needed()
    return pd.read_csv(DATA_PATH, sep=";")


def regression_metrics(y_true: pd.Series, y_pred: np.ndarray) -> dict[str, float]:
    mse = mean_squared_error(y_true, y_pred)
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": float(np.sqrt(mse)),
        "R2": r2_score(y_true, y_pred),
    }


def save_metrics(metrics: dict[str, dict[str, float]]) -> None:
    rows = []
    for model_name, values in metrics.items():
        row = {"model": model_name}
        row.update(values)
        rows.append(row)
    metrics_df = pd.DataFrame(rows)
    metrics_df.to_csv(OUTPUT_DIR / "model_metrics.csv", index=False, encoding="utf-8-sig")
    print(metrics_df.to_string(index=False))


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    plt.figure(figsize=(11, 9))
    sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm", annot=True, fmt=".2f", square=True)
    plt.title("Wine Quality Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=200)
    plt.close()


def plot_predictions_with_interval(
    y_true: pd.Series,
    y_pred: np.ndarray,
    residual_std: float,
    filename: str,
) -> None:
    order = np.argsort(y_pred)
    sorted_pred = y_pred[order]
    sorted_true = np.asarray(y_true)[order]
    interval = 1.96 * residual_std

    plt.figure(figsize=(11, 6))
    plt.scatter(range(len(sorted_true)), sorted_true, s=22, alpha=0.65, label="Actual quality")
    plt.plot(sorted_pred, color="#1f77b4", linewidth=2, label="Predicted quality")
    plt.fill_between(
        range(len(sorted_pred)),
        sorted_pred - interval,
        sorted_pred + interval,
        color="#1f77b4",
        alpha=0.18,
        label="Approx. 95% prediction interval",
    )
    plt.xlabel("Test samples sorted by predicted value")
    plt.ylabel("Wine quality")
    plt.title("Actual vs Predicted Wine Quality")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=200)
    plt.close()


def plot_selected_features(selected_features: list[str], scores: np.ndarray) -> None:
    selected_scores = pd.DataFrame({"feature": selected_features, "score": scores})
    selected_scores = selected_scores.sort_values("score", ascending=True)

    plt.figure(figsize=(9, 5))
    plt.barh(selected_scores["feature"], selected_scores["score"], color="#2a9d8f")
    plt.xlabel("SelectKBest f_regression score")
    plt.title("Selected Features")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "selected_features.png", dpi=200)
    plt.close()


def main() -> None:
    ensure_directories()
    df = load_data()

    print("Dataset shape:", df.shape)
    print("\nMissing values:")
    print(df.isna().sum())
    print("\nDescriptive statistics:")
    print(df.describe().T)

    plot_correlation_heatmap(df)

    target = "quality"
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
    )

    baseline_model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("regressor", LinearRegression()),
        ]
    )
    baseline_model.fit(X_train, y_train)
    baseline_pred = baseline_model.predict(X_test)
    baseline_residual_std = float(np.std(y_test - baseline_pred, ddof=1))

    k = 8
    feature_model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("selector", SelectKBest(score_func=f_regression, k=k)),
            ("regressor", LinearRegression()),
        ]
    )
    feature_model.fit(X_train, y_train)
    feature_pred = feature_model.predict(X_test)
    feature_residual_std = float(np.std(y_test - feature_pred, ddof=1))

    selector = feature_model.named_steps["selector"]
    selected_mask = selector.get_support()
    selected_features = X.columns[selected_mask].tolist()
    selected_scores = selector.scores_[selected_mask]

    pd.Series(selected_features, name="selected_features").to_csv(
        OUTPUT_DIR / "selected_features.csv",
        index=False,
        encoding="utf-8-sig",
    )
    plot_selected_features(selected_features, selected_scores)

    metrics = {
        "Linear Regression - all features": regression_metrics(y_test, baseline_pred),
        f"Linear Regression - top {k} selected features": regression_metrics(y_test, feature_pred),
    }
    save_metrics(metrics)

    plot_predictions_with_interval(
        y_test,
        baseline_pred,
        baseline_residual_std,
        "prediction_interval_all_features.png",
    )
    plot_predictions_with_interval(
        y_test,
        feature_pred,
        feature_residual_std,
        "prediction_interval_selected_features.png",
    )

    print("\nSelected features:")
    for feature in selected_features:
        print(f"- {feature}")

    print(f"\nOutputs saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
