import socket

def receive_file(receiver_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver_socket:
        receiver_socket.bind(('0.0.0.0', receiver_port))
        receiver_socket.listen()
        print("Waiting for sender...")
        sender_socket, sender_address = receiver_socket.accept()
        print("Connected to sender.")

        data = sender_socket.recv(1024)
        if data == b'file_transfer_flag':
            with open('received_file.txt', 'wb') as file:
                while True:
                    chunk = sender_socket.recv(1024)
                    if not chunk:
                        break
                    file.write(chunk)
            print("File received successfully.")
        else:
            print("Received message:", data.decode())
                  

receiver_port = 12346

receive_file(receiver_port)
