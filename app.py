# app.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonif(message="Hello level 400 FET, Quality Assurance!")


if __name__ == '__main__':
    app.run(debug=True)
