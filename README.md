# 🛡️ CyberPulse-Suite: Automated Security Audit & Reconnaissance Framework

CyberPulse-Suite is a modular, multi-threaded security assessment engine written in Python. It consolidates network reconnaissance, vulnerability identification, web application security testing, and digital forensic log parsing into a unified, actionable **Executive Summary Report**.


## 🌟 Key Features

- **Modular Architecture:** Isolated modules ensure independent execution without cascading script failures.
- **Part 1 - Network Reconnaissance:** Scans active network ports and flags unencrypted or legacy protocols (Telnet, FTP, HTTP).
- **Part 2 - Vulnerability Assessment:** Analyses endpoint infrastructure for cryptographic vulnerabilities and known system risks.
- **Part 3 - Web Application Security:** Audits web interfaces for misconfigurations, missing HTTP security headers, and common web threats.
- **Part 4 - Digital Forensics & Log Audit:** Parses system authorization logs (`auth.log`) to identify potential brute-force or unauthorized access attempts.
- **Executive Audit Engine:** Automatically consolidates security findings, ranks risks by severity (**HIGH**, **MEDIUM**, **LOW**), and generates structured `.txt` and `.json` reports.


## 🏗️ Directory Layout

```text
CyberPulse-Suite/
├── modules/
│   ├── part1_recon.py        # Module 1: Reconnaissance
│   ├── part2_vuln.py         # Module 2: Vulnerability Assessment
│   ├── part3_web.py          # Module 3: Web Application Security
│   └── part4_forensics.py    # Module 4: Digital Forensics
├── reports/                  # Generated Findings Output
├── main.py                   # Master Orchestrator Engine
└── README.md                 # Project Documentation
