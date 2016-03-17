#coding=utf8

from bottle import (Bottle, run, request)
#from ..tables import TbAuth, DBSession


app = Bottle()

print(__name__)

@app.route(path='/hello_world', method=['GET'])
def hello_world():
    return "Hello world!\n ansbile 是不是很吊 哈哈"


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=10001, reloader=True)

