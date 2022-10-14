

from socket import *
from time import  sleep
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 6789))

while True:
    data = client.recv(1024)
    # if not data:
    #     break
    print(data.decode('utf-8'))
    sleep(0.1)
    client.close()

