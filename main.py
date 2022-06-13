#!/usr/bin/env python
# https://github.com/avnyadav/wafer_circleci
from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard
import json

app= Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "Flask app is running and I am changing"

port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
