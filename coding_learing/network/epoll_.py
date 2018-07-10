# -*- coding: utf-8 -*-
"""
Created on Wed May  2 01:17:00 2018

@author: vict
"""
import socket
import select

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',8888))
s.listen(5)
epoll_check = select.epoll()
epoll_check.register(s.fileno(),select.EPOLLIN | select.EPOLLET)
clientTuple_dic = {}
clientTuple_dic[s.fileno()] = (s,('',8888))

try:
    while True:
        epoll_check_lis = epoll_check.poll() #检测事件触发了的文件描述符及对应事件类型
        for fd,event in epoll_check_lis:
            if event == select.EPOLLIN:     #套接字可读       
                if fd == s.fileno():
                    newClient,newAddr = clientTuple_dic[fd][0].accept()
                    epoll_check.register(newClient.fileno(),select.EPOLLIN | select.EPOLLET)
                    clientTuple_dic[newClient.fileno()] = (newClient,newAddr)
                    print newAddr,'上线了！'
                else:
                    ClientSock,ClientAddr = clientTuple_dic[fd]
                    recvData = ClientSock.recv(1024)
                    if recvData:
                        print '接收到了',ClientAddr,'的数据：',recvData
                    else:
                        epoll_check.unregister(fd)
                        clientTuple_dic[fd][0].close()
                        print ClientAddr, '下线了！'
                        del clientTuple_dic[fd]
finally:
    s.close()
 