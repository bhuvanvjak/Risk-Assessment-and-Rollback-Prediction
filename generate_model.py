# generate_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dummy training data
X = pd.DataFrame({
    "files_changed": [1, 5, 10],
    "lines_added": [10, 100, 500],
    "deployment_hour": [2, 14, 22]
})
y = [0, 1, 1]  # 0 = success, 1 = rollback

model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("app/model/risk_model.pkl", "wb") as f:
    pickle.dump(model, f)
