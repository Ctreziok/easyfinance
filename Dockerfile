FROM python:3.12-slim

# Set environment variables and working directory
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=main.py

WORKDIR /app

#Installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copying rest of the code
COPY . .

#Exposing port 8080
EXPOSE 8080

#Running the app with Flask on port 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
