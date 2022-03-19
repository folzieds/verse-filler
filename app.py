from flask import Flask, render_template, request, redirect, url_for
from flask_material import Material
import json
import verseFiller

app = Flask(__name__)
Material(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/fill')
def fill_verse():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        verseFiller.upload_file(uploaded_file)
        verseFiller.fill_verse_inplace(uploaded_file.filename)
        verseFiller.download_file(uploaded_file)
    else:
        pass
    #download file and delete upon download
    return redirect(url_for('index'))

@app.get('/api/v1/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}