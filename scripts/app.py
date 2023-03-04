from flask import Flask, request, jsonify
from flask_cors import CORS
from sudoku import solve
app = Flask(__name__)
cors = CORS(app)

@app.route("/receiver", methods=["POST"])
def postME():
    data = request.get_json()
    result = solve(data['sudoku'], data['size'])
    data = jsonify(result)
    return data

if __name__ == '__main__':
    app.run(debug=True)