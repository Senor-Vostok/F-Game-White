import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '178.214.248.81'
port = 2020
s.connect((host, port))
s.send('hello!'.encode())
data = s.recv(1000000)
print('received', data, len(data), 'bytes')
s.close()