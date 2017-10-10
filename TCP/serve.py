#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import time

    
def tcplink(sock,addr):
    print('Accept new connnection from %s : %s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connnection from %s : %s closed...' % addr)
    
# 创建TCP协议，流形式的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定本机ip，端口
s.bind(('127.0.0.1',9999))
# 开始监听
s.listen(3)
print('Waiting for connnection...')

while True:
    sock,addr = s.accept()
    # 创建线程 响应client的socket
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
    

