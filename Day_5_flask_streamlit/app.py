from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route("/test-api", methods=["POST"])
def test_api():
    data = request.json

    url = data.get("url")
    method = data.get("method", "GET")
    payload = data.get("payload", {})
    headers = data.get("headers", {})

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        start = time.time()

        if method == "POST":
            response = requests.post(url, json=payload, headers=headers)
        else:
            response = requests.get(url, headers=headers)

        end = time.time()

        result = {
            "status_code": response.status_code,
            "response_time_ms": round((end - start) * 1000, 2),
            "headers": dict(response.headers),
        }

        # try JSON response
        try:
            result["body"] = response.json()
        except:
            result["body"] = response.text[:1000]  # limit output

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)