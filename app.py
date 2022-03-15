from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>test</h1>"

@app.route('/api/v1/health')
def health():
    return json.dumps({"Status": True})