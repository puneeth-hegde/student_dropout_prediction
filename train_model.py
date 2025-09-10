# train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import joblib

def load_data(path="student_dropout_clean.csv"):
    """Load cleaned dataset"""
    df = pd.read_csv(path)
    return df

def preprocess_features(df):
    """Split features & target, encode categorical features"""
    X = df.drop("Target", axis=1)
    y = df["Target"]
    
    # Encode categorical features
    for col in X.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
    
    return X, y

def train_models(X_train, y_train):
    """Train multiple models and return them in a dictionary"""
    models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=200, random_state=42)
    }
    
    for name, model in models.items():
        model.fit(X_train, y_train)
    
    return models

def evaluate_models(models, X_test, y_test):
    """Evaluate models and return a dictionary with scores"""
    results = {}
    for name, model in models.items():
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds, average="weighted")
        results[name] = {"accuracy": acc, "f1": f1}
        print(f"\n{name}")
        print("Accuracy:", acc)
        print("F1 Score:", f1)
        print(classification_report(y_test, preds))
    return results

def save_best_model(models, results, filename="student_dropout_model.pkl"):
    """Save the best model (highest F1 score)"""
    best_model_name = max(results, key=lambda x: results[x]["f1"])
    best_model = models[best_model_name]
    joblib.dump(best_model, filename)
    print(f"\n✅ Best model saved as {filename} ({best_model_name})")
    return best_model_name

def main():
    df = load_data()
    X, y = preprocess_features(df)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    models = train_models(X_train, y_train)
    results = evaluate_models(models, X_test, y_test)
    save_best_model(models, results)

if __name__ == "__main__":
    main()
