import socket
import struct
import threading

HEADER_FORMAT = '!HHIBBBH'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
HOST = '127.0.0.1'
PORT = 5000

