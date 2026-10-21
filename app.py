
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My DevOps Project</title>
    </head>
    <body>
        <h1>My First DevOps Project</h1>
        <p>Application is running successfully!</p>
        <a href="/health">Check application health</a>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "cloud-native-devops"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
