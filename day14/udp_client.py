'''
基于udp协议的echo客户端
'''

from  socket import  *

client = socket(AF_INET, SOCK_DGRAM)
while True:
    data_str = input('请输入：')
    client.sendto(data_str.encode('utf-8'), ('127.0.0.1', 10000))
    data , addr = client.recvfrom(1024)
    data_str = data.decode('utf-8')
    print('服务器响应 %s' % data_str)
    if data_str == 'bye':
        break
client.close()







#
# from socket import *
#
# client = socket(AF_INET, SOCK_DGRAM)
# while True:
#     data_str = input('请输入: ')
#     client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
#     data, addr = client.recvfrom(1024)
#     data_str = data.decode('utf-8')
#     print('服务器回应:', data_str)
#     if data_str == 'bye':
#         break
# client.close()
