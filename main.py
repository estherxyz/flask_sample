from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import datetime
import time
import json
import requests
import re

"""
Flask api sample.
"""


app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    # response.headers['Content-Type'] = 'application/json'

    return response


@app.route("/", methods=['GET','POST'])
def test():
    """
    """
    str_msg = 'hello'

    return jsonify({'msg': str_msg}), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

