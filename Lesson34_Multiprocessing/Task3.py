import socket
from multiprocessing import Process

HOST = '127.0.0.1'
PORT = 65432


def handle_client(connection, address):
    print(f"[INFO] Connected by {address}")
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"[DEBUG] Received {data} from {address}")
            connection.sendall(data)  # Echo back the data
    print(f"[INFO] Connection closed by {address}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[INFO] Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            process = Process(target=handle_client, args=(conn, addr))
            process.start()
            conn.close()


if __name__ == "__main__":
    main()
