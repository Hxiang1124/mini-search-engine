from flask import Flask, request, jsonify
from search_engine import build_index, search

app = Flask(__name__)

docs = [
    "python is great",
    "java is also great",
    "python and java",
    "python python java"
]

index = build_index(docs)

@app.route("/search")
def search_api():
    query = request.args.get("q", "")
    results = search(query, index)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)