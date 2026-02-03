Day 2:
- Cleaned LinkedIn profile
- Defined focus: Security + AI
- Plan: build daily small tools

Focus:
- Security + AI
- Building small, learning in public

Learning today:
- What port scanning is
- How tools like Nmap discover open ports
- Difference between TCP and UDP scans

Nmap Overview
Nmap (Network Mapper) is a free, essential tool used for scanning networks to find live hosts and perform enumeration, which is the process of gathering detailed information about hacking targets. It can be installed on Windows, Mac OS, and Linux.

--------------------------------------------------------------------------------
Core Scanning Commands
• Host Discovery (-sP): Instead of pinging devices one by one, this command automates the process to find all live hosts on an entire network quickly.
• TCP Connect Scan (-sT): This performs a full open scan by completing the TCP three-way handshake (SYN, SYN-ACK, and ACK) to confirm if a port is open.
• Stealth (SYN) Scan (-sS): Also known as a half-open scan, this is designed to be more "stealthy" to avoid detection by firewalls or Intrusion Detection Systems (IDS). It starts the handshake but sends a reset (RST) packet before the connection is fully established.

--------------------------------------------------------------------------------
Detailed Enumeration
• OS Detection (-O): This command enables nmap to guess the operating system (such as Windows or Linux) running on a target machine.
• Aggressive Scan (-A): This is a powerful "combo" command that performs OS detection, version detection of services (like Apache or SSH), script scanning, and a traceroute all at once.
• Port Specific Scanning (-p): You can target specific ports, such as port 80 or 443, to identify potential web servers.

--------------------------------------------------------------------------------
Advanced Features & Evasion
• Decoys (-D): This uses obfuscation to hide your tracks. By specifying decoy IP addresses, nmap sends traffic from multiple sources at once, making it difficult for a network admin to tell which IP is the real scanner.
• Nmap Scripting Engine (NSE): Users can run custom scripts for automation.
• Vulnerability Scanning (--script vuln): This automatically checks targets against a list of known vulnerabilities (CVEs) to see if they can be exploited.
• Timing (-T): You can adjust the speed of the scan from T0 to T5. Slower scans (like T1) are useful for avoiding detection, while higher speeds are faster but more noticeable.

Next steps:
- Write a simple Python port scanner
- Run basic Nmap scans on a test host
