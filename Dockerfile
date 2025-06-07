FROM python:3.11-slim

WORKDIR /app

# Install gcc and update pip to avoid C-extension build issues
RUN apt-get update && apt-get install -y gcc \
    && pip install --upgrade pip \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first to leverage caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc && apt-get autoremove -y

# Copy the rest of the app
COPY . .

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "app/main.py"]
