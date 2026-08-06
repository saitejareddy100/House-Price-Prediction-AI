from pathlib import Path

import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
data_path = Path("dataset/Housing.csv")

if not data_path.exists() or data_path.stat().st_size == 0:
    sample_data = pd.DataFrame(
        {
            "price": [250000, 320000, 410000, 275000, 360000, 495000, 290000],
            "area": [1200, 1800, 2400, 1500, 2000, 2600, 1700],
            "bedrooms": [2, 3, 4, 3, 4, 5, 3],
            "bathrooms": [1, 2, 3, 2, 3, 4, 2],
            "stories": [1, 2, 2, 1, 2, 3, 2],
            "mainroad": ["yes", "yes", "yes", "yes", "yes", "yes", "yes"],
            "guestroom": ["no", "yes", "no", "no", "yes", "no", "yes"],
            "basement": ["no", "yes", "yes", "no", "yes", "yes", "no"],
            "hotwaterheating": ["no", "no", "yes", "no", "no", "yes", "no"],
            "airconditioning": ["no", "yes", "yes", "no", "yes", "yes", "no"],
            "parking": [1, 2, 2, 1, 2, 3, 1],
            "prefarea": ["no", "yes", "yes", "no", "yes", "yes", "no"],
            "furnishingstatus": ["semi-furnished", "furnished", "semi-furnished", "unfurnished", "furnished", "semi-furnished", "unfurnished"],
        }
    )
    data_path.parent.mkdir(parents=True, exist_ok=True)
    sample_data.to_csv(data_path, index=False)
    print("Created a sample housing dataset because the original file was empty.")


df = pd.read_csv(data_path)

# Convert Yes/No columns
binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
]

for col in binary_columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"yes": 1, "no": 0, "1": 1, "0": 0, "true": 1, "false": 0})
    )
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

# One-Hot Encode furnishing status
df = pd.get_dummies(df, columns=["furnishingstatus"], drop_first=True)

# Features and Target
X = df.drop("price", axis=1)
y = df["price"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model
output_path = Path("house_price_model.pkl")
joblib.dump(model, output_path)

print(f"House Price Model Saved Successfully at {output_path.resolve()}!")