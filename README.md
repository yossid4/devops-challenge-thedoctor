````markdown
# DevOps Challenge – TheDoctor

This project is a proof-of-concept (POC) Flask application that securely fetches a `secretCode` value from an AWS DynamoDB table and exposes it via a REST API.

The app is fully Dockerized, tested, and built using Travis CI, with automatic deployment to Docker Hub.

## 🔧 Features

- Flask REST API with two endpoints:
  - `/secret`: returns the secret code from DynamoDB
  - `/health`: returns service and repo info
- Secure AWS credential handling via `.env`
- Dockerized with support for `docker-compose`
- CI/CD with Travis CI and Docker Hub integration
- Minimal unit tests for service availability
- CloudFormation template for bonus AWS deployment

## 📦 Technologies

- Python 3.11
- Flask
- AWS DynamoDB (via boto3)
- Docker / Docker Compose
- Travis CI

## 🚀 Quick Start (Local)

```bash
# 1. Copy and edit credentials
cp .env.example .env

# 2. Run the app locally
docker-compose up
````

Then visit:

* `http://localhost:5000/secret`
* `http://localhost:5000/health`

## 🧪 Run Tests

```bash
docker build -t thedoctor .
docker run --env-file .env thedoctor python -m unittest discover tests
```

## 📜 Endpoints

| Endpoint  | Method | Description                       |
| --------- | ------ | --------------------------------- |
| `/secret` | GET    | Returns secret code from DynamoDB |
| `/health` | GET    | Returns container and repo info   |

## 🛡️ Security

* `.env` is **ignored in Git** (`.gitignore`)
* Travis CI uses **secure environment variables**
* Never expose AWS keys in the repo or image

## 📄 Files

* `.env.example` – example config
* `Dockerfile` – production-ready build
* `docker-compose.yml` – dev environment
* `.travis.yml` – CI/CD configuration
* `verification.sh` – endpoint validation script

## ✅ License

MIT License

````

---

## 📄 `INSTRUCTIONS.md`

```markdown
# How to Use This Project

Follow these steps to run, test, and deploy the project.

---

## 🚀 Run Locally

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
````

2. **Edit `.env` with your real AWS credentials:**

   ```env
   AWS_ACCESS_KEY_ID=...
   AWS_SECRET_ACCESS_KEY=...
   ```

3. **Run using Docker Compose:**

   ```bash
   docker-compose up
   ```

---

## 🧪 Running Unit Tests

To run unit tests in a container:

```bash
docker build -t thedoctor .
docker run --env-file .env thedoctor python -m unittest discover tests
```

---

## 🔁 Rebuild If You Change Code

```bash
docker-compose build
```

---

## 🧪 Validate App (Manual)

After running:

```bash
curl http://localhost:5000/secret
curl http://localhost:5000/health
```

Or run:

```bash
bash verification.sh
```

---

## 📦 Environment Variables Reference

| Key                     | Description                   |
| ----------------------- | ----------------------------- |
| `AWS_ACCESS_KEY_ID`     | Your AWS access key           |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret key           |
| `AWS_REGION`            | AWS region (e.g. `eu-west-1`) |
| `DDB_TABLE`             | DynamoDB table name           |
| `CODE_NAME`             | Key to query in the table     |

---