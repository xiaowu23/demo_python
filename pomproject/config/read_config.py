# -*- coding:utf-8 -*-

import configparser      #python3将ConfigParser改为configparser
import os

#获取当前文件所在的路径
current_path = os.path.dirname(os.path.realpath(__file__))
#print(current_path)

#拼接配置文件的路径
config_path = os.path.join(current_path, 'config.ini')
print(config_path)

#实例化ConfigParser类
conf = configparser.ConfigParser()
conf.read(config_path)

smtp_server = conf.get("email","smtp_server")
#print(smtp_server)
port = int(conf.get("email", "port"))
#print(port, type(port))
sender = conf.get("email", "sender")
pwd = conf.get("email", "pwd")
receiver = conf.get("email", "receiver")
