from flask import Flask, request, render_template, jsonify
from flask_restful import Api, marshal
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

from controllers.controller import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=3000)
