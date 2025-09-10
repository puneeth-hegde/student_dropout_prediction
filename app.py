# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_dropout_model.pkl")

app = FastAPI(title="Student Dropout Prediction API")

# Define expected input schema
class StudentData(BaseModel):
    Marital_status: int
    Application_mode: int
    Application_order: int
    Course: int
    Daytime_evening_attendance: int
    Previous_qualification: int
    Previous_qualification_grade: float
    Nacionality: int
    Mothers_qualification: int
    Fathers_qualification: int
    Mothers_occupation: int
    Fathers_occupation: int
    Admission_grade: float
    Displaced: int
    Educational_special_needs: int
    Debtor: int
    Tuition_fees_up_to_date: int
    Gender: int
    Scholarship_holder: int
    Age_at_enrollment: int
    International: int
    Curricular_units_1st_sem_credited: int
    Curricular_units_1st_sem_enrolled: int
    Curricular_units_1st_sem_evaluations: int
    Curricular_units_1st_sem_approved: int
    Curricular_units_1st_sem_grade: float
    Curricular_units_1st_sem_without_evaluations: int
    Curricular_units_2nd_sem_credited: int
    Curricular_units_2nd_sem_enrolled: int
    Curricular_units_2nd_sem_evaluations: int
    Curricular_units_2nd_sem_approved: int
    Curricular_units_2nd_sem_grade: float
    Curricular_units_2nd_sem_without_evaluations: int
    Unemployment_rate: float
    Inflation_rate: float
    GDP: float

@app.get("/")
def read_root():
    return {"message": "Student Dropout Prediction API is running."}

@app.post("/predict")
def predict(data: StudentData):
    # Convert input data to DataFrame
    df = pd.DataFrame([data.dict()])

    # Rename columns to match training CSV exactly
    df.columns = [
        "Marital status",
        "Application mode",
        "Application order",
        "Course",
        "Daytime/evening attendance\t",
        "Previous qualification",
        "Previous qualification (grade)",
        "Nacionality",
        "Mother's qualification",
        "Father's qualification",
        "Mother's occupation",
        "Father's occupation",
        "Admission grade",
        "Displaced",
        "Educational special needs",
        "Debtor",
        "Tuition fees up to date",
        "Gender",
        "Scholarship holder",
        "Age at enrollment",
        "International",
        "Curricular units 1st sem (credited)",
        "Curricular units 1st sem (enrolled)",
        "Curricular units 1st sem (evaluations)",
        "Curricular units 1st sem (approved)",
        "Curricular units 1st sem (grade)",
        "Curricular units 1st sem (without evaluations)",
        "Curricular units 2nd sem (credited)",
        "Curricular units 2nd sem (enrolled)",
        "Curricular units 2nd sem (evaluations)",
        "Curricular units 2nd sem (approved)",
        "Curricular units 2nd sem (grade)",
        "Curricular units 2nd sem (without evaluations)",
        "Unemployment rate",
        "Inflation rate",
        "GDP"
    ]

    # Make prediction
    prediction = model.predict(df)

    return {"prediction": prediction[0]}
