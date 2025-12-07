import socket  

def scan(target,ports):
    print(f"\n Starting scan for str({target})")
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress,port):
    try:
        sock=socket.socket()
        sock.connect((ipaddress,port))      #tries to find the comp using ip,find the right servic(using port), knock on door,start talking if someone answer
        print("[+] port opened "+ str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter target to scan(seperate the target by ','):")
ports=int(input("[*] Enter how many ports you want to scan :"))
if ',' in targets:
    print("[*] scanning multiple targets...")
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '),ports)
else:
    scan(targets,ports)