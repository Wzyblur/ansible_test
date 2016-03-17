#coding=utf8

from bottle import run
from werkzeug.serving import run_simple

from app.bottle_app import app as bottle_app
from app.flask_app import app as flask_app


if __name__ == '__main__':
    #run(bottle_app, host='0.0.0.0', port=10000, reloader=True)
    run_simple('0.0.0.0', 10001, flask_app, use_reloader=True, use_debugger=True)

