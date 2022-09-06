import base64

with open('mm.jpg', 'rb') as f:
    data = f.read()
    print('字节数：', len(data))
    print(base64.b64encode(data))

with open('girl.jpg', 'wb') as f:
    f.write(data)
print('写入完成')