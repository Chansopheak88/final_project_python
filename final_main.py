from dns_lookup import get_ip_simple
from whois_module import whois_lookup
from port_scanner import scan_port
from http_header import HTTPHeaderGrabber
from file_handler import save_report

def main():
    print("============================")
    print("    MINI RECON TOOL v1     ")
    print("============================\n")

    domain = input("[*] Enter target domain: ").strip()

    print("\n[1] Resolving domain → IP...")
    ip = get_ip_simple(domain)

    if not ip:
        print("[!] Could not resolve domain.")
        return

    print(f"[✓] Resolved IP: {ip}")

    print("\n[2] Running WHOIS Lookup...")
    whois_data = whois_lookup(domain)

    print("\n[3] Running Port Scan (1–100)...")
    open_ports = []
    for p in range(1, 101):
        if scan_port(ip, p):
            open_ports.append(f"[+] Port {p} is OPEN")

    if not open_ports:
        open_ports.append("No open ports found in range 1–100")

    print("\n[4] Fetching HTTP headers...")
    header_grabber = HTTPHeaderGrabber(ip)
    header80 = header_grabber.get_headers(80)
    header443 = header_grabber.get_headers(443)

    print("[✓] Headers collected.")

    print("\n[5] Saving report...")
    report_file = save_report(
        ip,
        dns_result=f"Domain: {domain} -> IP: {ip}",
        whois_result=whois_data,
        port_results=open_ports,
        http_headers=[header80, header443]
    )

    print(f"[✓] Report saved: {report_file}")
    print("\nRecon complete.")


if __name__ == "__main__":
    main()