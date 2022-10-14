from threading import  Thread
from json import dumps
from socket import socket
from base64 import b64encode
def main():
    class FileTransferHandler(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self._client.send(json_str.encode('utf-8'))
            self._client.close()

    server = socket()
    server.bind(('127.0.0.1', 5566))
    server.listen(512)
    with open('guido.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        cli, addr = server.accept()
        FileTransferHandler(cli).start()

if __name__ == '__main__':
    main()
