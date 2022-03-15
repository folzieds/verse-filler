from flask import Flask, render_template
from flask_material import Material
import json
import verseFiller

app = Flask(__name__)
Material(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/fill')
def fill_verse(filename):
    verseFiller.fill_verse_inplace(filename)
    verseFiller.downloadFile(filename)
    #download file and delete upon download

@app.get('/api/v1/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}