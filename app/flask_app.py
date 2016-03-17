#coding=utf8

from flask import Flask, url_for, render_template, redirect, request
from werkzeug.serving import run_simple

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/ansible/hello', methods=['GET'])
def hello():
    for k, v in request.headers.items():
        print(str(k)+': '+str(v))
    import time
    time.sleep(1)
    return url_for('static', filename='index.html')

@app.route('/ansible/helloworld', methods=['GET'])
def helloworld():
    #return render_template('index1.html')
    #return redirect('http://recruitfiles.oss-cn-qingdao.aliyuncs.com/1603/0135018c799c91fa656446144d83df17.jpg', code=302)
    return redirect('http://recruitfiles.oss-cn-qingdao.aliyuncs.com/1602/e79a731bf10d785093e2f81b52252d7b.doc', code=302)
    #return redirect(url_for('static', filename='test.txt'), code=302)

@app.route('/ansible/helloworlds', methods=['GET'])
def helloworlds():
    return render_template('index1.html', name='piaotiejun')


if __name__ == '__main__':
    run_simple('0.0.0.0', 10000, app, use_reloader=True, use_debugger=True)
