import socket

#function that can call to look up a domain
def whois_lookup(domain: str):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #af_inet->internet address, sock_stream->tcp
    s.connect(("whois.iana.org",43))
    s.send(f"{domain}\r\n".encode())    #\r\n=end of message, encode()->turn the text into bytes
    response=s.recv(4096).decode() #means “give me up to 4096 bytes of your answer”, .decode()=turn bytes back to text
    s.close()
    return response

#print(whois_lookup("google.com"))