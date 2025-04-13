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