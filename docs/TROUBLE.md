```markdown
# 🛠️ Troubleshooting Guide

This file documents common issues encountered while building, testing, or deploying this project using Docker and Travis CI.

---

## 🚫 1. APT Post-Invoke Error

**Error:**
```

E: Problem executing scripts APT::Update::Post-Invoke ...
E: Sub-process returned an error code

```

**Cause:**
Occurs when running `apt-get update` on minimal base images (`python:3.11-slim`) due to post-invoke cleanup scripts.

**Solution:**
- Switch from `python:3.11-slim` to full `python:3.11` base image.
- This avoids needing to install `gcc`, libc-dev, or handle broken APT behavior manually.

---

## 🧵 2. RuntimeError: can't start new thread

**Error:**
```

RuntimeError: can't start new thread

````

**Cause:**
`pip` uses threaded progress bars that can crash in low-resource Travis environments.

**Solution:**
- Upgrade the Travis image to a newer distro:
  ```yaml
  dist: focal
````

* Disable rich pip progress bar inside the Dockerfile:

  ```dockerfile
  ENV PIP_NO_PROGRESS_BAR=off
  ```

---

## 🐳 3. Docker Build Fails on Travis

**Error:**

```
docker: Error response from daemon: pull access denied...
```

**Cause:**

* Travis fails to build or run the image because `docker build` failed earlier.
* This often stems from broken APT installs, missing tools, or incomplete requirements.

**Solution:**

* Fix image issues (see above), then ensure the Travis job fails if `docker build` fails:

  ```yaml
  script:
    - docker build -t $IMAGE_NAME . || exit 1
  ```

---

## 🔒 4. Travis CI Asking for Plan on Public Repo

**Issue:**
Despite using a public repo, Travis prompts you to select a paid plan.

**Cause:**
Travis now uses usage-based pricing. Public repos still need a plan selected (even if \$0).

**Solution:**

* Log in to [Travis CI](https://travis-ci.com/account/usage)
* Under “Plan,” ensure you’ve selected the free tier for public repositories.

---

## 🧪 5. Tests Don't Run – Image Not Found

**Error:**

```
Unable to find image 'thedoctor:latest' locally
```

**Cause:**
`docker build` failed, but the test step still runs.

**Solution:**
Make sure build failure stops the pipeline:

```yaml
script:
  - docker build -t $IMAGE_NAME . || exit 1
  - docker run ...  # only runs if build succeeded
```

---

*Last updated: June 2025*

```
