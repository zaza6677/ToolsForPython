#!/bin/python
import socket
target_host="127.0.0.1"
target_port=9998
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto("hello zaza6677",(target_host,target_port))
data,addr=client.recvfrom(4096)
print data

