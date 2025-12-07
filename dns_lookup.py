import socket
import sys

def get_ip_simple(domain):
    try:
        ip= socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python dns_lookup.py <domain_name>")
        print("\nExample: python dns_lookup.py google.com")
        sys.exit(1)
    
    domain = sys.argv[1]
    
    print(f"\n{'='*60}")
    print(f"Domain to IP Address Lookup: {domain}")
    print(f"{'='*60}\n")
    ip = get_ip_simple(domain)
    if ip:
        print(f"  IP Address: {ip}")
    else:
        print(f"  Could not resolve domain: {domain}")

if __name__ == "__main__":
    main()