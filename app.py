from flask import Flask, jsonify, request
from flask_cors import CORS
import matcher as matcher

app = Flask(__name__)
CORS(app)

@app.route("/matcher", methods = ['POST'])
def match():
    return matcher.web(request.form["answer"])