from socket import*

server_sockat - socket(AF_INET, SOCK_STREAM)
server_socket.bind("localhost", 12346)
server_sockat.listen(1)

connection, adres = server_sockat.accept()
print("f")
c = connection.recv(1024). decode()

if c == 'h':
    connection.send("iyg".encode())

connection.close()
server_sockat.close()
