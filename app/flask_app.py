#coding=utf8

from flask import Flask, url_for, render_template
from werkzeug.serving import run_simple

flask_app = Flask(__name__)
flask_app.config['DEBUG'] = True

@flask_app.route('/hello', methods=['GET'])
def hello():
    return url_for('static', filename='index.html')

@flask_app.route('/helloworld', methods=['GET'])
def helloworld():
    return render_template('/static/index.html')

@flask_app.route('/helloworlds', methods=['GET'])
def helloworlds():
    return render_template('index1.html', name='piaotiejun')


if __name__ == '__main__':
    run_simple('0.0.0.0', 8000, flask_app, use_reloader=True, use_debugger=True)
