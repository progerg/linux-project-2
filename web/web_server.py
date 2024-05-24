from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/status', methods=['GET'])
def get_status():
    status = {"status": "healthy"}
    return jsonify(status), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
