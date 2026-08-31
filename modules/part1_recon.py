import socket

def run_recon(target_ip):
    print("\n[--- PART 1: Network Reconnaissance ---]")
    common_ports = {21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS"}
    open_ports = []
    detected_issues = []
    
    for port, service in common_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[!] Open Port Identified: {port} ({service})")
            open_ports.append({"port": port, "service": service})
            
            if port == 23:
                detected_issues.append({
                    "severity": "HIGH",
                    "issue": "Insecure Telnet Protocol Active",
                    "description": "Telnet transmits data in plaintext. Recommendation: Migrate to SSH (Port 22)."
                })
            elif port == 21:
                detected_issues.append({
                    "severity": "MEDIUM",
                    "issue": "Unencrypted FTP Port Exposed",
                    "description": "FTP sends credentials in cleartext. Recommendation: Upgrade to SFTP/FTPS."
                })
        s.close()
    
    return {"open_ports": open_ports, "issues": detected_issues}
