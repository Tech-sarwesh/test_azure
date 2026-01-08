from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/messages", methods=["POST"])
def messages():
    data = request.json
    user_text = data.get("text", "")
    return jsonify({"text": f"You said: {user_text}"})

if __name__ == "__main__":
    app.run(port=3978)
