from flask import Flask, jsonify, request
import matcher as matcher

app = Flask(__name__)

@app.route("/matcher", methods = ['POST'])
def match():
    return matcher.web(request.form["answer"])