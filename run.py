#!/usr/bin/python
#coding=utf8

import os

os.popen('apt-get install openssh-server').read()
os.popen('apt-get install python-pip').read()
os.popen('pip install ansible').read()

uname = os.popen('whoami').read().strip()
os.popen('ssh-copy-id %s@127.0.0.1'%uname)

yaml = open('./deploy.yaml', 'r').readlines()
remote_user = yaml[2].replace('piaotiejun', uname)
yaml[2] = remote_user

out = open('deploy.yaml', 'w')
for line in yaml:
    out.write(line)
