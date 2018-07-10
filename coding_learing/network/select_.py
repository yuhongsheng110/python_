# -*- coding: utf-8 -*-
"""
Created on Wed May  2 01:16:27 2018

@author: vict
"""

import select
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8899))
s.listen(5)
inputs = [s]
inputs_addr_dic = {}  #用来记录地址的
try:
    while True:
        readable,writeable,exceable = select.select(inputs,[],[])
        
        for sock in readable:
            if sock == s:
                #新客户端
                newSock,newAddr = sock.accept()
                inputs.append(newSock)
                inputs_addr_dic[id(newSock)] = newAddr
                print newAddr,'上线了！'
            else:
                recvData = sock.recv(1024)
                if recvData:
                    print '收到',inputs_addr_dic[id(sock)],'的消息:',recvData
                else:
                    print inputs_addr_dic[id(sock)],'下线了！'
                    sock.close()
                    inputs.remove(sock)
finally:
    s.close()