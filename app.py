from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "AI Scam Detector",
        "status": "Backend is running",
        "features": [
            "URL Scanner",
            "Message Checker",
            "Email Checker",
            "Safety Guidelines"
        ]
    })


@app.route("/scan-url", methods=["POST"])
def scan_url():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "URL is required"}), 400

    return jsonify({
        "feature": "URL Scanner",
        "submitted_url": url,
        "status": "Needs further security verification",
        "note": "This demo does not verify the URL's actual safety."
    })


@app.route("/check-message", methods=["POST"])
def check_message():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message is required"}), 400

    return jsonify({
        "feature": "Message Checker",
        "message_received": True,
        "status": "Ready for scam analysis"
    })


@app.route("/check-email", methods=["POST"])
def check_email():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "").strip()

    if not email:
        return jsonify({"error": "Email is required"}), 400

    return jsonify({
        "feature": "Email Checker",
        "email_received": True,
        "status": "Ready for email analysis"
    })


@app.route("/safety-guidelines")
def safety_guidelines():
    return jsonify({
        "guidelines": [
            "Never share your password or OTP.",
            "Verify website addresses before opening them.",
            "Do not trust unexpected prize messages.",
            "Report suspicious emails and messages."
        ]
    })


if __name__ == "__main__":
    app.run()
