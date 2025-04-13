import socket
import struct
import threading

# Define the header structure: 13 bytes total
HEADER_FORMAT = '!HHIBBBH'  # Source port, Dest port, Seq num, ACK, SYN, FIN, Payload size
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

HOST = '127.0.0.1'
PORT = 5000

# Unpack the header from received binary data
def parse_header(data):
    return struct.unpack(HEADER_FORMAT, data)

# Determine server response based on control flags
def build_response(header):
    _, _, _, ack, syn, fin, payload_size = header
    if syn == 1:
        return "SYN received – connection initiated"
    elif ack == 1:
        return "ACK received – message acknowledged"
    elif fin == 1:
        return "FIN received – connection closing"
    else:
        return f"Data received – payload length: {payload_size}"

# Handle communication with a single client
def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data or len(data) < HEADER_SIZE:
                break  # Disconnect or invalid message

            # Separate header and payload
            header_data = data[:HEADER_SIZE]
            payload = data[HEADER_SIZE:]

            try:
                header = parse_header(header_data)
            except struct.error:
                print(f"[!] Malformed header from {addr}")
                break

            # Build and send appropriate response
            print(f"[>] Header from {addr}: {header}")
            response = build_response(header)
            print(f"[<] Response to {addr}: {response}")
            conn.sendall(response.encode())
    finally:
        conn.close()
        print(f"[-] Disconnected from {addr}")

# Start the server and accept clients in separate threads
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

if __name__ == "__main__":
    main()
