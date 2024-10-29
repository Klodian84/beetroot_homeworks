import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("UDP Server is up and listening on port 12345")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received message from {client_address}: {data.decode()}")
    message = f"Hello, client! I received your message: {data.decode()}"
    server_socket.sendto(message.encode(), client_address)
