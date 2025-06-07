from flask import Flask, jsonify
from app.dynamo import get_secret

app = Flask(__name__)

@app.route("/secret", methods=["GET"])
def secret():
    return jsonify({"secret_code": get_secret()})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "container": "https://hub.docker.com/repository/docker/yossid4/thedoctor/general (private)",
        "project": "https://github.com/yossid4/devops-challenge-thedoctor"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
