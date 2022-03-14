from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>test</h1>"

@app.route('/health')
def health():
    pass