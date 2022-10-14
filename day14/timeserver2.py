'''
套接字- 基于TCP协议创建时间服务器
'''
from socket import *
from time import *

# family=AF_INET - IPv4地址
# family=AF_INET6 - IPv6地址
# type=SOCK_STREAM - TCP套接字
# type=SOCK_DGRAM - UDP套接字
# type=SOCK_RAW - 原始套接字
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 6789))
server.listen()
print('服务器已经启动正在监听客户端连接.')
while True:
    client, addr = server.accept()
    print('客户端%s:%d连接成功.' % (addr[0], addr[1]))
    currtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()
