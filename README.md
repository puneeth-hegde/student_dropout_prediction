

# 🎓 Student Dropout Prediction API

This project is an **end-to-end machine learning system** to predict whether a student will **graduate, dropout, or continue studies**, based on demographic, academic, and socio-economic factors.

It provides a **REST API (FastAPI)** that can be run locally or inside a **Docker container**, and has been published to **GitHub Container Registry (GHCR)** for portability.

---

## 📊 Dataset

The dataset used is the **UCI Student Dropout dataset** (open-source).
It contains anonymized student information such as:

* Demographics (age, gender, nationality)
* Socio-economic (parents’ occupation, qualifications)
* Academic performance (grades, credits, admission score)
* External factors (GDP, inflation, unemployment)

Target variable:

* **Graduate**
* **Dropout**
* **Enrolled (still studying)**

---

## 📂 Project Structure

```
student_dropout/
│
├── app.py                      # FastAPI app serving predictions
├── train_model.py              # Script to train & save ML model
├── student_dropout_model.pkl   # Trained model
├── data.csv                    # Original dataset (ignored in GitHub)
├── student_dropout_clean.csv   # Cleaned dataset
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image definition
├── 01_student_dropout_EDA.ipynb    # Exploratory Data Analysis
├── 02_student_dropout_training.ipynb  # Model training notebook
└── README.md                   # Project documentation
```

> Note: Large datasets (`*.csv`) and virtual environments (`.venv/`) are ignored in GitHub.

---

## ⚙️ Setup and Run Locally

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/student_dropout.git
cd student_dropout
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI server

```bash
uvicorn app:app --reload
```

Open Swagger UI at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🐳 Run with Docker

### Build image

```bash
docker build -t student-dropout-api .
```

### Run container

```bash
docker run -p 8000:8000 student-dropout-api
```

Access Swagger UI:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🚀 Run from GitHub Container Registry (GHCR)

We pushed the container image to **GHCR**, so anyone can pull and run it without building.

### 1. Authenticate with GHCR

```bash
echo <YOUR_GITHUB_TOKEN> | docker login ghcr.io -u <YOUR_GITHUB_USERNAME> --password-stdin
```

### 2. Pull the image

```bash
docker pull ghcr.io/puneeth-hegde/student-dropout-api:latest
```

### 3. Run the container

```bash
docker run -p 8000:8000 ghcr.io/puneeth-hegde/student-dropout-api:latest
```

---

## 🌍 About GHCR

**GitHub Container Registry (GHCR)** is a container hosting service by GitHub.

* We used GHCR to **publish our Docker image** so it can be run on any machine.
* This makes our ML API portable and deployable to any cloud platform (AWS, Azure, GCP, etc).

---

## 🧠 What This Project Does

✅ Predicts if a student will **Graduate / Dropout / Enrolled**
✅ API interface via **FastAPI** (Swagger UI included)
✅ Reproducible Docker setup
✅ Portable image on **GitHub Container Registry (GHCR)**

---

## 🔮 Future Improvements

* Deploy API on **AWS Lambda + API Gateway** for serverless inference
* CI/CD pipeline with **GitHub Actions** for automated builds & pushes
* Extend dataset to support **real-time student data**
* Add monitoring dashboard for prediction insights
* Experiment with **deep learning models** (e.g., Neural Networks)

---

## 👨‍💻 Author

**Puneeth Hegde**
ML Engineer | Student Dropout Prediction API Project

---

