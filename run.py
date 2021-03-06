#!/usr/bin/python
#coding=utf8

import os

try:
    os.popen('mkdir ~/temp').read()
except:
    pass

try:
    os.popen('apt-get install openssh-server').read()
except:
    pass

try:
    os.popen('apt-get install python-pip').read()
except:
    pass

try:
    os.popen('pip install ansible').read()
except:
    pass

uname = os.popen('whoami').read().strip()
os.popen('ssh-copy-id %s@127.0.0.1'%uname)

yaml = open('./deploy.yaml', 'r').readlines()
remote_user = yaml[2].replace('piaotiejun', uname)
yaml[2] = remote_user

out = open('deploy.yaml', 'w')
for line in yaml:
    out.write(line)
