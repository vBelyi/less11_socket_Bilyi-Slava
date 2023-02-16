import socket

sock_server = socket.socket()
sock_server.bind(('127.0.0.1', 40))
sock_server.listen()

print('Chat is open')

conn, add = sock_server.accept()
name = 'AI'
client = (conn.recv(1024)).decode()
print('connected ' + client)
conn.send(name.encode())

while True:
    data = input('AI: ')
    conn.send(data.encode())
    data = conn.recv(1024)
    data = data.decode()
    print(client, ':', data)