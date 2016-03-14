#coding=utf8

from bottle import run
from werkzeug.serving import run_simple

from app.bottle_app import app
from app.flask_app import flask_app


if __name__ == '__main__':
    #run(app, host='0.0.0.0', port=10001, reloader=True)
    run_simple('0.0.0.0', 10001, flask_app, use_reloader=True, use_debugger=True)

