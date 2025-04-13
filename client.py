import socket
import struct

HEADER_FORMAT = '!HHIBBBH'
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def create_header(source_port, dest_port, seq, ack, syn, fin, payload):
    payload_size = len(payload)
    return struct.pack(HEADER_FORMAT, source_port, dest_port, seq, ack, syn, fin, payload_size)

