````markdown
# 🧪 Setup & Usage Instructions

This guide explains how to build, test, and run the project both locally and via CI/CD.

---

## 📦 Prerequisites

- Python 3.11+
- Docker installed and running
- AWS credentials with access to DynamoDB
- Docker Hub account (for pushing images)
- (Optional) Travis CI account linked to your GitHub repo

---

## 🚧 Local Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/devops-challenge-thedoctor.git
   cd devops-challenge-thedoctor
````

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set required environment variables:**

   ```bash
   export AWS_ACCESS_KEY_ID=your_key
   export AWS_SECRET_ACCESS_KEY=your_secret
   export AWS_REGION=eu-west-1
   export DDB_TABLE=your_table_name
   export CODE_NAME=your_code_name
   ```

4. **Run the app locally:**

   ```bash
   python app/main.py
   ```

5. **Run tests:**

   ```bash
   python -m unittest discover tests
   ```

---

## 🐳 Docker Usage

### Build the Docker image

```bash
docker build -t thedoctor .
```

### Run the container

```bash
docker run -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID=your_key \
  -e AWS_SECRET_ACCESS_KEY=your_secret \
  -e AWS_REGION=eu-west-1 \
  -e DDB_TABLE=your_table \
  -e CODE_NAME=your_code \
  thedoctor
```

---

## 🔄 CI/CD with Travis CI

1. Add your Travis CI secrets in project settings:

   * `DOCKER_USER`
   * `DOCKER_PASS`
   * `AWS_ACCESS_KEY_ID`
   * `AWS_SECRET_ACCESS_KEY`
   * `AWS_REGION`
   * `DDB_TABLE`
   * `CODE_NAME`

2. Push to `main` branch. Travis will:

   * Build the Docker image
   * Run tests inside the container
   * Push the image to Docker Hub if tests pass

---

## 🌐 API Endpoint

* **GET /secret**
  Returns a secret value for the provided `CODE_NAME` from DynamoDB.

---
