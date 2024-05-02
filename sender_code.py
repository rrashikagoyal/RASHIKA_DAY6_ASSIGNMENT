import socket

def send_file(filename, receiver_ip, receiver_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
        sender_socket.connect((receiver_ip, receiver_port))
        sender_socket.sendall(b'file_transfer_flag')  # Sending a flag indicating it's a file transfer
        with open(filename, 'rb') as file:
            sender_socket.sendfile(file, 0)
        print("File sent successfully.")

# Example usage:
sender_ip = 'sender_ip_address'
sender_port = 12345
receiver_ip = 'receiver_ip_address'
receiver_port = 12346

send_file('file_to_send.txt', receiver_ip, receiver_port)
