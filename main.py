import json
import os
from modules.part1_recon import run_recon
from modules.part2_vuln import run_vuln_scan
from modules.part3_web import run_web_tests
from modules.part4_forensics import run_forensics_collection

def generate_summary_report(all_issues):
    high_count = sum(1 for i in all_issues if i['severity'] == 'HIGH')
    med_count = sum(1 for i in all_issues if i['severity'] == 'MEDIUM')
    low_count = sum(1 for i in all_issues if i['severity'] == 'LOW')

    summary_text = "\n" + "="*50 + "\n"
    summary_text += "          EXECUTIVE SECURITY SUMMARY REPORT          \n"
    summary_text += "="*50 + "\n"
    summary_text += f"Total Identified Findings: {len(all_issues)}\n"
    summary_text += f" [🔴 HIGH]: {high_count} | [🟠 MEDIUM]: {med_count} | [🟡 LOW]: {low_count}\n"
    summary_text += "-"*50 + "\n\n"

    if not all_issues:
        summary_text += "[✓] No critical issues detected! Target system appears secure.\n"
    else:
        summary_text += "DETAILED PROBLEM FINDINGS:\n"
        for idx, issue in enumerate(all_issues, 1):
            summary_text += f"\n{idx}. [{issue['severity']}] {issue['issue']}\n"
            summary_text += f"   - Description: {issue['description']}\n"

    summary_text += "\n" + "="*50 + "\n"
    return summary_text

def main():
    target_ip = "127.0.0.1"
    os.makedirs("./reports", exist_ok=True)

    print("==================================================")
    print("   CYBERPULSE AUTOMATED SECURITY AUDIT SUITE      ")
    print("==================================================")

    part1 = run_recon(target_ip)
    part2 = run_vuln_scan(target_ip)
    part3 = run_web_tests(target_ip)
    part4 = run_forensics_collection()

    all_detected_issues = (
        part1.get("issues", []) +
        part2.get("issues", []) +
        part3.get("issues", []) +
        part4.get("issues", [])
    )

    summary_report = generate_summary_report(all_detected_issues)
    print(summary_report)

    full_output = {
        "target": target_ip,
        "summary": {
            "total_issues": len(all_detected_issues),
            "issues_list": all_detected_issues
        },
        "raw_results": {
            "reconnaissance": part1,
            "vulnerabilities": part2,
            "web_security": part3,
            "forensics": part4
        }
    }

    with open("./reports/security_audit_summary.json", "w") as json_file:
        json.dump(full_output, json_file, indent=4)

    with open("./reports/security_audit_summary.txt", "w") as txt_file:
        txt_file.write(summary_report)

    print("[✓] Executive Report saved to: ./reports/security_audit_summary.txt")
    print("[✓] Complete JSON findings saved to: ./reports/security_audit_summary.json")

if __name__ == "__main__":
    main()
