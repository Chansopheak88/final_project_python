import datetime

def save_report(target_ip, dns_result, whois_result, port_results, http_headers):
    """
    Save all scan results into a single .txt file.
    """
    filename = f"scan_report_{target_ip}.txt"
    timestamp = datetime.datetime.now()

    with open(filename, "w", encoding="utf-8") as f:
        f.write("===== Mini Recon Tool Report =====\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Target IP: {target_ip}\n\n")

        f.write("===== DNS Resolution =====\n")
        f.write(dns_result + "\n\n")

        f.write("===== WHOIS Lookup =====\n")
        f.write(whois_result + "\n\n")

        f.write("===== Port Scan Result =====\n")
        for p in port_results:
            f.write(p + "\n")

        f.write("\n===== HTTP Header (Port 80) =====\n")
        f.write(http_headers[0] + "\n\n")

        f.write("===== HTTP Header (Port 443) =====\n")
        f.write(http_headers[1] + "\n")

    return filename