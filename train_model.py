import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Create synthetic dataset
def generate_data(n_samples=1000, seed=42):
    np.random.seed(seed)
    data = {
        "files_changed": np.random.poisson(15, n_samples),
        "test_coverage": np.random.randint(30, 100, n_samples),
        "dependencies": np.random.poisson(5, n_samples),
        "previous_failures": np.random.randint(0, 5, n_samples),
        "change_type": np.random.randint(0, 5, n_samples),       # feature, bugfix, hotfix, refactor, config
        "deployment_time": np.random.randint(0, 4, n_samples),   # morning, afternoon, evening, night
    }

    df = pd.DataFrame(data)

    # Simulate target: risk (1 = rollback, 0 = safe)
    risk_score = (
        (df["files_changed"] > 25).astype(int) * 0.2 +
        (df["test_coverage"] < 60).astype(int) * 0.3 +
        (df["dependencies"] > 7).astype(int) * 0.1 +
        (df["previous_failures"] > 1).astype(int) * 0.3 +
        (df["change_type"] == 2).astype(int) * 0.2 +  # hotfix
        (df["deployment_time"] == 3).astype(int) * 0.2  # night
    )

    # Final label
    df["rollback"] = (risk_score > 0.5).astype(int)

    return df

# 2. Train model
def train_and_save_model():
    df = generate_data()

    X = df.drop("rollback", axis=1)
    y = df["rollback"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model trained with accuracy: {acc:.2f}")
    print(classification_report(y_test, y_pred))

    # 3. Save model
    model_dir = "app/model"
    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "risk_model.pkl"), "wb") as f:
        pickle.dump(model, f)
    print("✅ Model saved to app/model/risk_model.pkl")

if __name__ == "__main__":
    train_and_save_model()
