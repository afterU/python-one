'''
使用socketserver模块创建时间服务器
'''
from socketserver import TCPServer, StreamRequestHandler
from time import *

class TimeRequestHandler(StreamRequestHandler):
    def handle(self):
        current_time = localtime(time())
        time_str = strftime('%Y-%m-%d %H:%M:%S', current_time)
        self.wfile.write(time_str.encode('utf-8'))

server = TCPServer(('127.0.0.1', 6789), TimeRequestHandler)
server.serve_forever()