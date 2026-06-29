import joblib
from pathlib import Path

model = joblib.load(Path("../M1-B2/models/pyrenex_risk_v2.joblib"))
import pandas as pd

df = pd.read_csv("../M1-B2/data/lending_club_holdout.csv")

X = df.drop(columns=["loan_status"])
row = X.iloc[[0]]   # ✅ double crochets
proba = model.predict_proba(row)
print(proba)
