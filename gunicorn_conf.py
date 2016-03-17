#coding=utf8

# http://docs.gunicorn.org/en/latest/settings.html


import multiprocessing

# 监听端口
bind = '0.0.0.0:10000'

# 工作进程数  即gunicorn进程的数量(1) 另外有一个master进程 杀死gunicorn进程只需要杀死master进程即可 pid记录的也是master进程
workers = multiprocessing.cpu_count() * 2 + 1 # 工作进程9 master进程1

# 连接(等待被处理)数量上限(2048)
backlog =  1024 

# 工作模式(sync) [sync, eventlet, gevent, tornado]
worker_class = 'gevent'

# 每个工作进程开启的线程数(1)
threads = 1

# 处理中的并发量只对gevent和eventlet模式生效(1000)
work_connections = 1000

# 重启前处理的最大请求数量(0)
max_requests = 0

# 重启前的随机最大处理请求数(0, max_requests_jitter) 为了避免所有worker都同时重启
max_requests_jitter = 0

# 当workers超过这个时间没有响应时重启gunicorn(30s)
# 在同步模式下知道gunicorn会很久没有没有反应那么才可以设置较大的值
# 在非同步模式下代表确保处理一个请求不能超过该时间
timeout = 30

# 从接到重启命令后到重启间的时间(用以处理请求的时间)(30)
graceful_timeout = 30

# 长连接时间(2s)
keepalive = 2

# 请求行(resquest-_line)的最大字节数[0, 8190](4094)
# 一个HTTP请求报文由请求行（request line）、请求头部（header）、空行和请求数据4个部分组成
# 请求行由请求方法字段、URL字段和HTTP协议版本字段3个字段组成，它们用空格分隔
limit_request_line = 4094

# http header键值对最大数[0, 32768](100)
limit_request_fields = 100

# 一个http header字段的最大字节数[0, 8190](8190)
limit_request_field_size = 8190

# 代码改动时是否重启(False) 开发环境中使用
reload = True

# TODO
# 跟踪服务器执行的所有命令(False)
spew = False

# 检查配置(False)
check_config = False

# 预载wsgi app,在workers被fork之前加载app节省启动时间(False)
preload_app = False

# 守护进程 将app从终端分离出来并在后台执行(False)
daemon = True

# TODO
# 将变量传递到env([])
raw_env = []

# 保存gunicorn进程的pid文件路径(None)
pidfile = '/home/piaotiejun/temp/gunicorn.pid'

# TODO
# gunicorn启动使用的temp文件夹(默认文件夹None)
worker_tmp_dir = None

# 将gunicorn进程切换为另一个用户下(None) 参数为uid
user = None

# 将gunicorn进程切换为另一个用户组下(None) 参数为gid
group = None

# gunicorn生成的文件的umask(0)
# 默认一般是002 即从777 - 002 = 775
# 7是自己对文件的权限4(读)+2(写)+1(执行)
# 之后的5/5是与文件所有者同一组的用户的权限/不与文件所有者同组的其他用户的权限
umask = 0002 # 八进制

# TODO 测试结果不对 待测试
# 请求的ip安全列表逗号分隔('127.0.0.1')
#forwarded_allow_ips = '127.0.0.1,192.168.0.144'
forwarded_allow_ips = '1.12.0.1'
#forwarded_allow_ips = '*'

# access log文件路径 不识别~
accesslog = '/home/piaotiejun/temp/ansible_test/log/access.log'

# error log路径 不识别~
errorlog = '/home/piaotiejun/temp/ansible_test/log/error.log'

# access log文件一个记录的格式
"""
h       remote address
l       '-'
u       user name
t       date of the request
r       status line (e.g. GET / HTTP/1.1)
m       request method
U       URL path without query string
q       query string
H       protocol
s       status
B       response length
b       response length or '-' (CLF format)
f       referer
a       user agent
T       request time in seconds
D       request time in microseconds
L       request time in decimal seconds 处理请求用时
p       process ID
{Header}i       request header
{Header}o       response header
"""
#access_log_format = '{"status:" %(u)s, ""%(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(h)s %(p)s %({host}i)s %({Accept-Language}i)s %({X-Forwarded-For}i)s  %({X-Real-IP}i)s ""%({Host}i)s "service date:"%({Date}o)s}'

access_log_format = """{\
"request time in seconds": "%(T)s", \
"request time in microseconds": "%(D)s", \
"request time in decimal seconds": "%(L)s", \
"remote address": "%(h)s", \
"user name": "%(u)s", \
"date of request": "%(t)s", \
"status line": "%(r)s", \
"request method": "%(m)s", \
"url path without query string": "%(U)s", \
"query string": "%(q)s", \
"protocol": "%(H)s", \
"status": "%(s)s", \
"response length": "%(B)s", \
"response length or (CLF format)": "%(b)s", \
"referer": "%(f)s", \
"user agent": "%(a)s", \
"worker process id": "%(p)s", \
"X-Forwarded-For": "%({X-Forwarded-For}i)s", \
"X-Real-IP": "%({X-Real-IP}i)s", \
"Host": "%({Host}i)s", \
"": "%({}o)s"\
}"""

# 错误日志的输出级别[debug, info, warrning, error, critical](info)
loglevel = 'debug'

# 将gunicon log写入syslog(False)
# syslog的配置文件为/etc/syslog.conf 我的电脑ubuntu14.04保存在/etc/rsyslog.conf
syslog = False

# syslog输入地址 默认地址可以查看/etc/services('udp://localhost:514')
syslog_addr = 'tcp://localhost/514'

# 加入到python sys.path的模块(None) 多个模块之间逗号分隔 例如:'/home/djangoprojects/myproject,/home/python/mylibrary'
pythonpath = None

# TODO 测试结果不对 待测试
# 允许的代理请求ip,逗号分隔('127.0.0.1')
proxy_allow_ips = '127.0.0.1'

# TODO SSH设置

# hooks Called just before the master process is initialized
def on_starting(server):
    pass

# hooks Called to recycle workers during a reload via SIGHUP
def on_reload(server):
    pass

# hooks Called just after the server is started
def when_ready(server):
    pass

# hooks Called just before a worker is forked
def pre_fork(server, worker):
    pass

# hooks Called just after a worker has been forked
def post_fork(server, worker):
    pass

# hooks Called just after a worker has initialized the application
def post_worker_init(worker):
    pass

# hooks Called just after a worker exited on SIGINT or SIGQUIT
def worker_int(worker):
    pass

# hooks Called when a worker received the SIGABRT signal
def worker_abort(worker):
    pass

# hooks Called just before a new master process is forked
def pre_exec(server):
    pass

# hooks Called just before a worker processes the request
def pre_request(worker, req):
    worker.log.info("%s %s %s" % (req.method, req.path, str(req.__dict__)))

# hooks Called after a worker processes the request
def post_request(worker, req, environ, resp):
    pass

# hooks Called just after a worker has been exited
def worker_exit(server, worker):
    pass

# hooks Called just after num_workers has been changed
def nworkers_changed(server, new_value, old_value):
    pass

# hooks Called just before exiting Gunicorn
def on_exit(server):
    server.log.info("exit")
    open('/home/piaotiejun/temp/ansible_test/log/test.log', 'w').write(str(server.__dict__))
