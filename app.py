#coding=utf8

from bottle import (Bottle, run, request)


app = Bottle()


@app.route(path='/hello_world', method=['GET'])
def hello_world():
    return "Hello world!"


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=10000, reloader=True)

