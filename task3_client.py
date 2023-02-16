import socket

sock1 = socket.socket()

print('Chat is open')
name = input('Print your name: ')
sock1.connect(('127.0.0.1', 30))
sock1.send(name.encode())
server_name = sock1.recv(1024).decode()

print(server_name, 'connected')

while True:
    data = input(f'Client {name}: ')
    sock1.send(data.encode())
    data = (sock1.recv(1024)).decode()
    print(server_name, ':', data)
