# Design Explanation – TCP Header Simulation

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

## Server Design 

- Listens on a fixed port using TCP.
- Accepts multiple incoming connections.
- Each client is handled in a new thread using Python’s `threading.Thread`.
- Inside each thread:
  - The header is parsed using `struct.unpack`.
  - The appropriate response is determined based on the flags.
  - The server logs header and response info for each client.

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
- Each thread cleans up its own socket on disconnect or error.

---

## Design Rationale

- **Threaded model** allows concurrent clients without blocking.
- **Binary header format** simulates real TCP structure.


