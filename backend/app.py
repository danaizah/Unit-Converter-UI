from flask import Flask, request, jsonify
from flask_cors import CORS
from converter.converter_calculations import convert

app = Flask(__name__)
CORS(app)  # allows React to talk to Flask

@app.route("/convert", methods=["POST"])
def handle_convert():
    data = request.get_json()
    try:
        result = convert(data["value"], data["from_unit"], data["to_unit"])
        return jsonify({ "result": result })
    except ValueError as e:
        return jsonify({ "error": str(e) }), 400

if __name__ == "__main__":
    app.run(debug=True)

