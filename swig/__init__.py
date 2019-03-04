from flask import Flask, render_template
from flask_assets import Environment, YAMLLoader
from datetime import datetime

# Reference the app properly,
app = Flask(__name__)
# and initiate the bundle loader.
Environment(app).from_yaml(__name__ + '/static/bundles.yaml')

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
