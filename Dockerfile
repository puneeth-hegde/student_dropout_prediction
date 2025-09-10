# ============================
# Base image with Python 3.11
# ============================
FROM python:3.11-slim

# ============================
# Set working directory
# ============================
WORKDIR /app

# ============================
# Copy requirements first
# ============================
COPY requirements.txt .

# ============================
# Install Python dependencies
# ============================
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ============================
# Copy entire project into container
# ============================
COPY . .

# ============================
# Expose port 8000
# ============================
EXPOSE 8000

# ============================
# Run FastAPI using Uvicorn
# ============================
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
