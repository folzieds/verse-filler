from flask import Flask, render_template
import json

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/api/v1/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}