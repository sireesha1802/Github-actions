
import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "my-app")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


@app.route("/")
def home():
    return f"""
    <html>
        <head><title>{APP_NAME}</title></head>
        <body>
            <h1>Welcome to {APP_NAME}!</h1>
            <p>Environment: {ENVIRONMENT}</p>
            <p>Status: Application is running successfully but not get output from broswer.</p>
            <p><a href="/health">Health Check</a></p>
            <p><a href="/info">Application Info</a></p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME
    }), 200


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "environment": ENVIRONMENT,
        "framework": "Flask"
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
