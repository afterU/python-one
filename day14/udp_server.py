
'''
基于udp协议的echo服务器
'''

from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.1', 10000))
while True:
    data, addr = server.recvfrom(1024)
    print('接收到客户端的消息 %s' % data.decode('utf-8'))
    server.sendto(data, addr)

server.clise()