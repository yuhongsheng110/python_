#!/usr/bin/env python
# coding=utf-8
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print '1'
s.bind(('',8059))
print '2'
s.listen(5)
print '3'
s_new,s_new_addr = s.accept()
print '4'
while True:
    new_data = s_new.recv(1024)
    print s_new_addr,new_data
    if new_data == '1111':
        break

s_new.close()
s.close()   
