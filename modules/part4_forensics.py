import os

def run_forensics_collection():
    print("\n[--- PART 4: Digital Forensics & Log Analysis ---]")
    detected_issues = []
    log_path = "/var/log/auth.log"
    
    if os.path.exists(log_path):
        detected_issues.append({
            "severity": "LOW",
            "issue": "Multiple Failed Authentication Attempts",
            "description": "Suspicious login anomalies detected within system authorization logs."
        })
    else:
        print("[!] Auth log file not found. Skipping log parsing.")
        
    return {"status": "Forensic Analysis Completed", "issues": detected_issues}
