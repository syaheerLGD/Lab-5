import socket


s = socket.socket()


port = 8888
host = '192.168.0.200'


s.connect(('192.168.0.200', port))


data = s.recv(1024)


s.send(b'Hi saya client, Terima Kasih!')


print(data)


s.close()
