import socket
import struct

# Header format: source port, dest port, sequence number, ACK, SYN, FIN, payload size
HEADER_FORMAT = '!HHIBBBH'
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def create_header(source_port, dest_port, seq, ack, syn, fin, payload):
    payload_size = len(payload)
    # Pack the header into a binary structure
    return struct.pack(HEADER_FORMAT, source_port, dest_port, seq, ack, syn, fin, payload_size)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))

        # Define sample header values
        source_port = 12345
        sequence_number = 1
        ack, syn, fin = 0, 1, 0  # Set SYN flag to initiate connection
        payload = b"Hello, server!"

        # Create and send message (header + payload)
        header = create_header(source_port, SERVER_PORT, sequence_number, ack, syn, fin, payload)
        message = header + payload
        s.sendall(message)

        # Receive and display server response
        response = s.recv(1024)
        print("Server response:", response.decode())

if __name__ == "__main__":
    main()
