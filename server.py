import socket
import struct
import threading

HEADER_FORMAT = '!HHIBBBH'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
HOST = '127.0.0.1'
PORT = 5000

def parse_header(data):
    return struct.unpack(HEADER_FORMAT, data)

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
    
def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data or len(data) < HEADER_SIZE:
                break

            header_data = data[:HEADER_SIZE]
            payload = data[HEADER_SIZE:]

            try:
                header = parse_header(header_data)
            except struct.error:
                print(f"[!] Malformed header from {addr}")
                break

            print(f"[>] Header from {addr}: {header}")
            response = build_response(header)
            print(f"[<] Response to {addr}: {response}")
            conn.sendall(response.encode())
    finally:
        conn.close()
        print(f"[-] Disconnected from {addr}")
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            client_thread.start()

if __name__ == "__main__":
    main()