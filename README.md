# CSC4200Prog2
Programming Assignment 2: TCP Header Simulation in Client-Server Communication

# TCP Header Simulation – Client-Server Communication

## Overview

This project simulates a simplified TCP-like communication between a client and server using Python. The client sends structured messages containing a 13-byte custom header, and the server parses the header and responds accordingly.

This project demonstrates:
- TCP/IP socket programming
- Binary message formatting using `struct`
- Control flag handling (SYN, ACK, FIN)

## Dependencies

- Python 3.8 or higher
- Standard libraries only:
  - `socket`
  - `struct`

## Project Structure

```
.
├── client.py                # Client implementation
├── server.py                # Server implementation
├── Makefile                 # Build/run/clean commands
├── README.md                # Project overview and instructions
└── design_explanation.md   # Protocol design and logic documentation
```

## Custom TCP-Like Header

Each message begins with a 13-byte binary header, followed by a payload.

| Field         | Size (bytes)  | Description                          |
|---------------|---------------|--------------------------------------|
| Source Port   | 2             | Client-side port                     |
| Dest Port     | 2             | Server's listening port              |
| Sequence No   | 4             | Sequence number                      |
| ACK Flag      | 1             | 0 or 1 – acknowledgment              |
| SYN Flag      | 1             | 0 or 1 – start handshake             |
| FIN Flag      | 1             | 0 or 1 – terminate                   |
| Payload Size  | 2             | Number of bytes in the payload       |

- **Total Header Size:** 13 bytes  
- **Struct Format:** `!HHIBBBH` (network byte order / big-endian)

## How to Run

Make sure Python is installed.

### Build (no-op for Python)
make build

### Run the server
make run-server


### Run the client (in another terminal)
make run-client

### Clean up
make clean

## Server Response Logic

The server responds based on the flags in the header:

- `SYN == 1` → `"SYN received – connection initiated"`
- `ACK == 1` → `"ACK received – message acknowledged"`
- `FIN == 1` → `"FIN received – connection closing"`
- Otherwise → `"Data received – payload length: X"`

## Notes

- Start the server **before** the client.
- You may modify flag values and payload in `client.py` for testing.
- Only one client connection is supported at a time.
- Graceful handling of disconnects and malformed headers is included.



