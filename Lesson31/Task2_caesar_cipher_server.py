import socket


def caesar_cipher(text: str, shift: int) -> str:
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("UDP Caesar Cipher Server is up and listening on port 12345")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message, key = data.decode().split(":", 1)
    shift_key = int(key)

    print(f"Received message from {client_address}: {message} with key: {shift_key}")

    encrypted_message = caesar_cipher(message, shift_key)
    print(f"Encrypted message to send back: {encrypted_message}")

    server_socket.sendto(encrypted_message.encode(), client_address)
