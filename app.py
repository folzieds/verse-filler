from flask import Flask, render_template, request, redirect, url_for, after_this_request
from flask_material import Material
import os
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
        @after_this_request
        def remove_file(response):
            try:
                os.remove(uploaded_file.filename)
            except Exception as error:
                app.logger.error("Error removing or closing downloaded file handle", error)
            return response
        verseFiller.download_file(uploaded_file)
    else:
        pass
    return redirect(url_for('index'))

@app.get('/api/v1/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}