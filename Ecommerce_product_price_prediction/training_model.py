import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# Step 1:load dataset
df = pd.read_csv(r"C:\Users\Hp\Downloads\ec_dataset.csv")
print(df.head())


# Step 2:data cleaning
print("missing values before cleaning:")
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype in ["int64", "float64"]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

y = df["final_price"]
X = df.drop("final_price", axis=1)
model_columns = X.columns.values


# Step 3:split data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("training samples:", X_train.shape)
print("testing samples:", X_test.shape)


# Step 4:model building(Random Forest)
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Step 5:model testing
y_pred = model.predict(X_test)
# Step 6: performance metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("R2 Score:", r2)
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

# Step 7:visualization
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.title("actual vs predicted price")
plt.show()
# Step 8: save model and columns(.pkl files)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model_columns.pkl", "wb") as f:
    pickle.dump(model_columns, f)

print("model and columns saved successfully.")
