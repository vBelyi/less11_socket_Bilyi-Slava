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
    res_list = ['buy', 'order', 'sell']
    res_list2 = ['site', 'website', 'link']
    data = input('AI: ')
    conn.send(data.encode())
    data = conn.recv(1024).decode()
    print(client, ':', data)
    if data.lower() in ('hey', 'hello', 'hi', 'privet', 'greeting'):
        data = 'How may I help you?'
        print(name, ': ', data)
        conn.send(data.encode())
        data = conn.recv(1024).decode()
        print(client, ': ', data)
    for i in data.lower().split():
        for j in res_list:
            if i == j:
                data = 'To buy our products please visit our website'
                conn.send(data.encode())
                print(name, ': ', data)
                data = conn.recv(1024).decode()
                print(client, ':', data)
    for a in data.lower().split():
        for b in res_list2:
            if a == b:
                data = 'This is our website: https://studyspace.com.ua/ '
                conn.send(data.encode())
                print(name, ': ', data)
                data = conn.recv(1024).decode()
                print(client, ':', data)


