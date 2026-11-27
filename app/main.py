from functools import wraps
import hmac
import os
import socket
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

raw_origins = os.environ.get("ALLOWED_ORIGINS", "*").strip()
if raw_origins == "*" or raw_origins == "":
    allowed_origins = "*"
else:
    allowed_origins = [
        origin.strip().rstrip("/")
        for origin in raw_origins.split(",")
        if origin.strip()
    ]

CORS(app, resources={r"/*": {"origins": allowed_origins}})


def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        expected_key = os.environ.get("API_KEY", "").strip()
        if not expected_key:
            return jsonify({"error": "Server API key not configured"}), 500

        provided_key = request.headers.get("X-API-Key", "").strip()
        if not provided_key or not hmac.compare_digest(provided_key, expected_key):
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated


@app.route("/")
def home():
    return jsonify({
        "service": "devops-starter-api",
        "status": "running",
        "hostname": socket.gethostname()
    }), 200


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
