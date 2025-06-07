```markdown
# 🧩 Troubleshooting Log

This document lists common issues encountered during the development and CI/CD process, along with their solutions.

---

## 1. 🔒 AccessDeniedException on DynamoDB

**Issue:**
```

The provided key element does not match the schema

````

**Cause:** Using `code_name` instead of correct camelCase `codeName` key. Also missing sort key if required.

**Fix:**
- Confirm table schema (e.g., via `describe-table`)
- Use `codeName` and correct key structure in `get_item`

---

## 2. 🐍 `KeyError: 'secret_code'` when accessing `/secret`

**Cause:** The DynamoDB item used `"secretCode"` instead of `"secret_code"` (case-sensitive mismatch)

**Fix:**
Update code to:
```python
return item["secretCode"]
````

---

## 3. 🐳 Docker build failed on Travis with pip-related error

**Issue:**

```
RuntimeError: can't start new thread
```

**Cause:** Travis CI's free tier build container has limited memory. Some Python packages like `MarkupSafe` or `cryptography` require compiling native C extensions from source.

**Fix:**
Install `gcc` before running `pip install`:

```dockerfile
RUN apt-get update && apt-get install -y gcc
```

**Optional:** Clean up after install to reduce image size:

```dockerfile
RUN apt-get update && apt-get install -y gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc && apt-get autoremove -y
```

---

## 4. ❌ Travis CI build failed with "invalid reference format"

**Cause:** Incorrect line continuation in `docker run` command inside `.travis.yml`

**Fix:** Break multi-line `docker run` into separate lines:

```yaml
- docker run \
    --env AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    --env AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    ...
```

---

## 5. 🕸️ Travis CI account error: "Owner not on a new pricing"

**Cause:** Travis CI requires manual approval or a request to enable credits for public repos.

**Fix:**

* Go to: [https://app.travis-ci.com/account/plan](https://app.travis-ci.com/account/plan)
* Click **"Request"** for public repo access
* Or email: `support@travis-ci.com` with your repo link

---

## 6. 🧪 Tests not failing the build in Travis

**Cause:** `|| true` in test command disables build failure on test errors

**Fix:** Remove `|| true` from `.travis.yml`:

```yaml
- docker run ... python -m unittest discover tests
```

---

```

Let me know if you'd like me to generate or update the file directly in a zipped project structure.
```
