from socket import socket


def main():
    client = socket()
    client.connect(('127.0.0.1', 6789))
    in_data = bytes()
    while True:
        data = client.recv(1024)
        while data:
            in_data += data
            data = client.recv(1024)
        print(in_data.decode('utf-8'))

if __name__ == '__main__':
    main()