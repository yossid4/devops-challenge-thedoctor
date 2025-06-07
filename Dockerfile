FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies early (cached if unchanged)
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Add app folder to PYTHONPATH
ENV PYTHONPATH=/app

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/main.py"]
