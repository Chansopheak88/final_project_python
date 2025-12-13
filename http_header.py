import socket
import ssl

class HTTPHeaderGrabber:
    def __init__(self, ip):
        self.ip = ip

    def get_headers(self, port=80):
        """
        Connect using socket and fetch HTTP headers.
        Supports HTTPS automatically for port 443.
        """
        try:
            # Create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)

            # Connect
            sock.connect((self.ip, port))

            # Wrap socket with SSL if HTTPS
            if port == 443:
                context = ssl.create_default_context()
                sock = context.wrap_socket(sock, server_hostname=self.ip)

            # Send GET request
            request = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(self.ip)
            sock.send(request.encode())

            # Receive response (only header part)
            response = sock.recv(4096).decode(errors="ignore")
            sock.close()

            # Split off only the headers
            header_section = response.split("\r\n\r\n")[0]

            return header_section

        except Exception as e:
            return f"[ERROR] Could not fetch headers: {str(e)}"