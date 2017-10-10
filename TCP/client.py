#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 创建TCP协议，流形式的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接本机ip，端口
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
s.send(b'xiaoqiang~')
print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()