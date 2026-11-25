import os
import socket
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow frontend origins (defaults to '*' for easy testing; lock down in production)
allowed_origins = os.environ.get("ALLOWED_ORIGINS", "*")
CORS(app, resources={r"/*": {"origins": allowed_origins}})

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
