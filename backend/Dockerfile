# 🐍 Use official Python base image
FROM python:3.11-slim

# 📁 Set the working directory inside the container
WORKDIR /app

# 📦 Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 🧠 Copy the entire project (make sure .dockerignore is clean)
COPY ./app ./app

# 🚀 Set the command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
