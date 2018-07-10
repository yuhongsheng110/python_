#!/usr/bin/env python
# coding=utf-8
import socket
import struct
import sys
if len(sys.argv)!= 2:
    print '-----'
    print type(sys.argv),'---',sys.argv
else:
    ip = sys.argv[1]

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sendAddr = (ip,69)
info = struct.pack('!H5sb5sb',1,'a.jpg',0,'octet',0)
udp_socket.sendto(info,sendAddr)
p_num = 0
recvFile = ''
cmd = -1
seq = 0 
while True:
    recvData,recvAddr = udp_socket.recvfrom(1024)
    print "recvAddr:",recvAddr
    recvDataLen = len(recvData)
    print 'recvDataLen:',recvDataLen
    r_unpack_tmp = struct.unpack('!HH',recvData[:4])
    seq = r_unpack_tmp[1]
    if r_unpack_tmp[0] == 3: #数据包
        if p_num == 0:
            f = open('b.jpg','a')
        if p_num + 1 == seq:
            f.write(recvData[4:])
            p_num += 1 
        print '收到数据：',p_num
        ackBuf = struct.pack('!HH',4,p_num)
        udp_socket.sendto(ackBuf,recvAddr)
    if recvDataLen < 516:
        f.close()
        print '下载完毕！'
        break
    elif cmd == 5:
        print 'error'
        break
udp_socket.close()


