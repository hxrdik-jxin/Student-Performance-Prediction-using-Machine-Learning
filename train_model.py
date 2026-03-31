import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocess import load_data, preprocess

# Load dataset
data = load_data("../data/student_data.csv")

# Preprocess
X, y = preprocess(data)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100)

# Training
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "../model/student_model.pkl")
