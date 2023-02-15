import socket

sock_server = socket.socket()
sock_server.bind(('127.0.0.1', 50))
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
    if data.lower() in ('hey', 'hello', 'hi'):
        data = 'How may I help you?'
        conn.send(data.encode())
        data = conn.recv(1024)
        data = data.decode()
        print(client, ':', data)
    elif data.lower() in ('i want to buy'):
        data = 'To buy something please visit our website'
        conn.send(data.encode())
        data = conn.recv(1024)
        data = data.decode()
        print(client, ':', data)
    else:
        data = input('AI: ')
        conn.send(data.encode())
        data = conn.recv(1024)
        data = data.decode()
        print(client, ':', data)
