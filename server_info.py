#!/usr/bin/env python3
from flask import Flask, jsonify # type: ignore
import socket
import os
import subprocess

app = Flask(__name__)

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return int(uptime_seconds)
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Server Info API",
        "endpoints": ["/hostname", "/uptime"]
    })

@app.route('/hostname')
def hostname():
    return jsonify({
        "hostname": socket.gethostname()
    })

@app.route('/uptime')
def uptime():
    return jsonify({
        "uptime_seconds": get_uptime()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
