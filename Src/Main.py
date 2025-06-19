from flask import Flask, request, jsonify
from kmath_engine import run_kmath_logic

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt", "")
    response = run_kmath_logic(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=8080)
