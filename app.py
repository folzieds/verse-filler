from flask import Flask, render_template, request, flash,redirect, url_for
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
import json
import verseFiller

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/help')
def help():
    return render_template('help.html')


@app.route('/api/v1/fill', methods = ['POST'])
def fill():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                flash('No file path')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected')
                return redirect(request.url)
            else:
                filename = secure_filename(file.filename)
                verseFiller.upload_file(file, filename)
                verseFiller.fill_verse_inplace(filename)
                # write file into io
                return verseFiller.download_file(filename) 
        except:
            app.logger.error("An Error occurred while processing file")

@app.get('/api/v1/health')
def health():
    return json.dumps({"Status": True}), 200, {"ContentType":"application/json"}