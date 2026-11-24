import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "devops-starter-api",
        "status": "running",
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/config")
def config():
    return jsonify({
        "app_env": os.environ.get("APP_ENV", "development"),
        "app_version": os.environ.get("APP_VERSION", "0.1.0")
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
