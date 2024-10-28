import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

message = "Hello, server!"
key = 3

formatted_message = f"{message}:{key}"
print(f"Sending message to server: {formatted_message}")
client_socket.sendto(formatted_message.encode(), server_address)

data, server = client_socket.recvfrom(1024)
print(f"Received encrypted response from server: {data.decode()}")

client_socket.close()
