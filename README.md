# Mini Reconnaissance Tool (Python)

## Overview
This tool performs basic reconnaissance tasks:
- DNS Lookup
- WHOIS Lookup
- Port Scanning
- HTTP Header / Banner Grabbing
- File Handling (save logs)

This project is designed according to the proposal requirements using:
- OOP (encapsulation + inheritance)
- socket library
- Python data structures
- error handling
- output logging

---

## How It Works

### 1. The user enters a domain
Example: google.com

### 2. DNS module resolves it into an IP
Used by all other modules.

### 3. WHOIS module retrieves information from:  
whois.iana.org

### 4. Port scanner checks ports 1–100 using sockets.

### 5. HTTP header grabber:
- Connects via TCP
- Sends GET / request
- Collects headers from ports 80 and 443

### 6. File handler:
Saves everything into: