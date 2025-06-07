
---

## 📄 `SUMMARY.md`

```markdown
# Summary of Development Process

This document outlines how the project was built and why certain choices were made.

---

## 1. Objective

Create a secure, containerized Flask application to extract a secret code from DynamoDB, with CI/CD integration via Travis and Docker Hub.

---

## 2. Tech Stack & Structure

- **Language:** Python 3.11
- **Web framework:** Flask
- **AWS SDK:** boto3
- **Containerization:** Docker + Compose
- **CI/CD:** Travis CI
- **Cloud provider:** AWS (via DynamoDB)

---

## 3. Development Workflow

1. ✅ Built core app using Flask
2. ✅ Integrated `boto3` to query DynamoDB with `codeName`
3. ✅ Configured `.env` for local secure credential handling
4. ✅ Dockerized the app (Dockerfile + Compose)
5. ✅ Created minimal `unittest` suite for basic health check
6. ✅ Integrated Travis CI:
   - Build Docker image
   - Run tests
   - Push image to Docker Hub
7. ✅ Wrote documentation and verification scripts
8. ✅ Bonus: added CloudFormation template (if applicable)

---

## 4. Challenges

- 🐛 Schema mismatch (`code_name` vs `codeName`)
- 🔐 Secure handling of AWS credentials in CI
- 🔍 Debugging missing fields from DynamoDB response

---

## 5. Deliverables

- ✅ GitHub repo with all code and docs
- ✅ Docker Hub image with working container
- ✅ CI pipeline via Travis
- ✅ `.env.example` and clear instructions
- ✅ Verification script
