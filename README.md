
# Student Dropout Prediction API

## Overview

This project predicts whether a student is likely to graduate or drop out based on academic and demographic features. The model is trained on an **open-source dataset** and served via a **FastAPI** backend. The project is containerized using **Docker** and the image is hosted on **GitHub Container Registry (GHCR)**, making it easy to run anywhere.

---

## Features

* Predict student outcome (`Graduate` or `Dropout`) from input features.
* Built with **Python**, **scikit-learn**, **FastAPI**, and **Pandas**.
* Containerized with **Docker** for reproducibility.
* GHCR-hosted Docker image for deployment on any system.

---

## Project Structure

```
student_dropout/
├─ app.py                     # FastAPI application
├─ train_model.py             # Script for training the ML model
├─ student_dropout_model.pkl   # Saved trained model
├─ requirements.txt           # Python dependencies
├─ Dockerfile                 # Docker configuration
├─ sample_payload.json        # Sample input for API testing
├─ data.csv                   # Dataset (not pushed to repo)
├─ .venv/                     # Python virtual environment (not pushed)
└─ README.md                  # Project documentation
```

> Note: Large files like datasets, virtual environment, and `.pkl` files are usually not pushed to GitHub. Only code, Dockerfile, requirements, and documentation are included.

---

## Prerequisites

* **Docker** installed on your system.
* Internet connection to pull the container from GHCR.
* (Optional) **Python 3.11** if you want to run locally without Docker.

---

## How to Run Locally (Optional)

1. Create a virtual environment and activate it:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn app:app --reload
```

4. Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

5. Test the API using `sample_payload.json`.

---

## How to Run via Docker

### **Step 1: Pull Docker Image**

The container is hosted on GHCR. Pull it using:

```bash
docker pull ghcr.io/puneeth-hegde/student-dropout-api:latest
```

### **Step 2: Run the Container**

```bash
docker run -d -p 8000:8000 ghcr.io/puneeth-hegde/student-dropout-api:latest
```

* The API will be available at `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`

### **Step 3: Test the API**

* Using `curl` (Windows PowerShell):

```powershell
$json = Get-Content .\sample_payload.json -Raw
Invoke-RestMethod -Uri http://127.0.0.1:8000/predict -Method POST -Body $json -ContentType "application/json"
```

* Using Swagger UI: Open `http://127.0.0.1:8000/docs` and click **Try it out**.

---

## Sample JSON Input (`sample_payload.json`)

```json
{
  "Marital_status": 1,
  "Application_mode": 15,
  "Application_order": 1,
  "Course": 9254,
  "Daytime_evening_attendance": 1,
  "Previous_qualification": 1,
  "Previous_qualification_grade": 160.0,
  "Nacionality": 1,
  "Mother_qualification": 1,
  "Father_qualification": 3,
  "Mother_occupation": 3,
  "Father_occupation": 3,
  "Admission_grade": 142.5,
  "Displaced": 1,
  "Educational_special_needs": 0,
  "Debtor": 0,
  "Tuition_fees_up_to_date": 1,
  "Gender": 0,
  "Scholarship_holder": 0,
  "Age_at_enrollment": 19,
  "International": 0,
  "Curricular_units_1st_sem_credited": 6,
  "Curricular_units_1st_sem_enrolled": 6,
  "Curricular_units_1st_sem_evaluations": 6,
  "Curricular_units_1st_sem_approved": 6,
  "Curricular_units_1st_sem_grade": 14.0,
  "Curricular_units_1st_sem_without_evaluations": 0,
  "Curricular_units_2nd_sem_credited": 6,
  "Curricular_units_2nd_sem_enrolled": 6,
  "Curricular_units_2nd_sem_evaluations": 6,
  "Curricular_units_2nd_sem_approved": 6,
  "Curricular_units_2nd_sem_grade": 13.666667,
  "Curricular_units_2nd_sem_without_evaluations": 0,
  "Unemployment_rate": 0,
  "Inflation_rate": 13.9,
  "GDP": -0.3
}
```

---

## Notes

* The Docker image contains **everything** needed to run the FastAPI API — no local Python environment or dependencies required.
* The model (`student_dropout_model.pkl`) is already packaged inside the Docker image.
* The API can run **anywhere Docker is installed**, making it portable across laptops, servers, or cloud platforms.

---

