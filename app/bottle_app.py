#coding=utf8

from bottle import (Bottle, run, request)
#from ..tables import TbAuth, DBSession
from db.tables import TbAuth, DBSession


app = Bottle()

print(__name__)

@app.route(path='/hello_world', method=['GET'])
def hello_world():
    session = DBSession()
    auths = session.query(TbAuth).all()
    ps = [a.permission for a in auths]
    print(ps)

    return "Hello world!\n ansbile 是不是很吊 哈哈"


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=10001, reloader=True)

