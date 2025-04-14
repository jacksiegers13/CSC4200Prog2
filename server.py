import socket
import struct

# Header format: 13 bytes
HEADER_FORMAT = '!HHIBBBH'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
HOST = '127.0.0.1'
PORT = 5000

# Unpack the header into individual fields
def parse_header(data):
    return struct.unpack(HEADER_FORMAT, data)

# Determine the server's response based on the header flags
def build_response(header):
    _, _, _, ack, syn, fin, payload_size = header
    if syn == 1:
        return "SYN received - connection initiated"
    elif ack == 1:
        return "ACK received - message acknowledged"
    elif fin == 1:
        return "FIN received - connection closing"
    else:
        return f"Data received - payload length: {payload_size}"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        # Accept a single client connection
        conn, addr = server.accept()
        print(f"[+] Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data or len(data) < HEADER_SIZE:
                    break  # No data or message too short

                # Separate and decode the header
                header_data = data[:HEADER_SIZE]
                payload = data[HEADER_SIZE:]

                try:
                    header = parse_header(header_data)
                except struct.error:
                    print("[!] Malformed header")
                    break

                print(f"[>] Received header: {header}")
                response = build_response(header)
                print(f"[<] Sending response: {response}")
                conn.sendall(response.encode())

        print(f"[-] Disconnected from {addr}")

if __name__ == "__main__":
    main()
