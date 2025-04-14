# Design Explanation – TCP Header Simulation (Single-Client)

## Header Format

The client constructs a 13-byte header using `struct.pack` with format string `!HHIBBBH`. This encodes:

- Source Port (2 bytes)
- Destination Port (2 bytes)
- Sequence Number (4 bytes)
- ACK, SYN, FIN Flags (1 byte each)
- Payload Size (2 bytes)

The final message sent is:  
`[13-byte header] + [payload]`

---

## Server Design (Single-Client)

- Listens on a fixed port using TCP.
- Accepts a single incoming connection.
- Receives and parses messages with a fixed 13-byte header.
- Responds based on the first-matching flag:
  - `SYN`: handshake
  - `ACK`: acknowledgment
  - `FIN`: connection close
  - Default: return payload length

The server logs all received headers and responses.

---

## Client Design

- Connects to the server’s IP and port.
- Constructs a header with user-defined values.
- Sends the header + payload in one transmission.
- Waits for and prints the server's response.

---

## Error Handling

- Ensures at least 13 bytes are received before parsing.
- Uses `try/except` to handle malformed data.
- Handles disconnects and exits cleanly.

---

