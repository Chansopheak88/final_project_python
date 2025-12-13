import socket  

def scan(target,ports):
    #scan many ports on a target ip add
    print(f"\n Starting scan for ({target})")
    for port in range(1,ports +  1):
        #use the scan port func to scan each port
        scan_port(target,port)
    print(f"\n[✓] scan complete for {target}")
    print(f"[✓] {ports} ports scanned successfully\n")

def scan_port(ipaddress,port):
    try:
        sock=socket.socket()
        sock.settimeout(1)  #put a time out on a socket before
        sock.connect((ipaddress,port))      #tries to find the comp using ip,find the right servic(using port), knock on door,start talking if someone answer
        print(f"[+] Port {port} is Open")
        sock.close()
        return True         #return true when done in case 
    except socket.timeout:
        return False
    except socket.error:
        return False
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")
        return False

def main():
    #main func only run when the codes are execute directly in its module
    targets=input("[*] Enter targets to scan (seperate by ','): ")
    ports = int(input("[*] Enter how many ports you want to scan: "))
    if ',' in targets:
        print("[*] Scanning multiple targets...")
        for ip_add in targets.split(','):
            scan(ip_add.strip(),ports)
    else:
        scan(targets,ports)

#this block only run when the script is execute directly 
if __name__ == "__main__":
    main()