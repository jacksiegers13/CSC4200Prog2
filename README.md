# TCP Header Simulation – Client-Server Application

## Overview

This project implements a simplified TCP-like client-server system using Python sockets. The client sends structured messages containing a custom 13-byte header, and the server parses this header to determine the correct response based on TCP-style control flags.

### Key Concepts:
- TCP socket programming
- Binary data formatting using `struct`
- Simulated control flags (SYN, ACK, FIN)

---

## Requirements

- Python 3.8+
- No external libraries (only `socket`, `struct`)

---

## Project Files

```
.
├── client.py                # Client implementation
├── server.py                # Single-client server implementation
├── Makefile                 # Build/run commands
├── README.md                # Project documentation
└── design_explanation.md   # Header structure and design rationale
```

---

## Header Structure

Each message contains:
- A fixed **13-byte header**
- A variable-length payload

| Field         | Size | Description                       |
|---------------|------|-----------------------------------|
| Source Port   | 2 B  | Client's port                     |
| Dest Port     | 2 B  | Server's listening port           |
| Sequence No   | 4 B  | Message sequence number           |
| ACK Flag      | 1 B  | Acknowledgment flag (0 or 1)      |
| SYN Flag      | 1 B  | Synchronization flag (0 or 1)     |
| FIN Flag      | 1 B  | Termination flag (0 or 1)         |
| Payload Size  | 2 B  | Size of the message payload       |

**Struct format:** `!HHIBBBH`

---

## How to Use

### Build (placeholder for Python):
```bash
make build
```

### Run the server:
```bash
make run-server
```

### Run the client:
```bash
make run-client
```

### Clean:
```bash
make clean
```

---

## Server Response Rules

The server returns specific messages based on the flags:

- `SYN == 1` → `"SYN received – connection initiated"`
- `ACK == 1` → `"ACK received – message acknowledged"`
- `FIN == 1` → `"FIN received – connection closing"`
- No flags → `"Data received – payload length: X"`

---

## Notes

- The server accepts one client connection at a time.
- Start the server **before** the client.
- You can modify flags and payload in `client.py`.
- Graceful handling of disconnects and malformed headers is included.

---

