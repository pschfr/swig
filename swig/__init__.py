from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Used to pass variables to every template
@app.context_processor
def inject_now():
    return { 'now': datetime.utcnow() }

# On main index route, or /<name>...
@app.route('/')
@app.route('/<name>')
def index(name=None):
    # Render index template, pass name to page.
    return render_template('index.html', name=name)
