import socket

sock_server = socket.socket()
sock_server.bind(('127.0.0.1', 30))
sock_server.listen()

print('Chat is open')

conn, add = sock_server.accept()
name = 'AI'
client = (conn.recv(1024)).decode()
print('connected ' + client)
conn.send(name.encode())

while True:
    data = conn.recv(1024).decode()
    print(client, ':', data)
    data = str(len(data.split()))
    print(name, ': ', data) #цю строку можна закоментувати, якщо не хочеться бачити повідомлення з кількістю слів в чаті серверу
    conn.send(data.encode())