import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"[{client_address}] {message.decode('utf-8')}")
        client_socket.sendall(message)

    client_socket.close()
    print(f"[DISCONNECT] {client_address} disconnected.")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
