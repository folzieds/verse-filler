from flask import Flask, render_template, request, flash,redirect, url_for, after_this_request
from werkzeug.utils import secure_filename
from flask_material import Material
import os
import json
import verseFiller

app = Flask(__name__)
Material(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.route('/test', methods = ['POST'])
def test():
    if request.method == 'POST':
        app.logger.error("This happened!!!")
    
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}

@app.route('/fill', methods = ['POST'])
def fill():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected')
                return redirect(request.url)
            else:
                filename = secure_filename(file.filename)
                verseFiller.upload_file(file, filename)
                verseFiller.fill_verse_inplace(filename)
                return verseFiller.download_file(filename)
        except:
            app.logger.error("An Error occured while processing file")

@app.get('/api/v1/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}