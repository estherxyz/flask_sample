from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import datetime
import time
import json
import requests
import re
import os
from pathlib import Path
from dotenv import load_dotenv


"""
Flask api sample.
"""


app = Flask(__name__)
app.config.from_pyfile('config/develop.cfg')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    # response.headers['Content-Type'] = 'application/json'

    return response


@app.route("/", methods=['GET','POST'])
def hello():
    """
    """
    str_msg = 'hello'

    return jsonify({'msg': str_msg}), 200



if __name__ == "__main__":
    # set env variable
    env_path = Path('.') / 'env' / 'develop.env'
    print('env_path', env_path)
    load_dotenv(dotenv_path=env_path)

    # get env variable
    env1 = os.getenv("ENV1")
    print('ENV1', env1)

    # run flask
    app.run()

