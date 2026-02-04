# Day 3 – Port Scanner CLI Tool

## Built
- Simple TCP port scanner in Python
- Packaged as a CLI tool using Poetry
- Exposed command: `portscan <host>`

## Implementation
- Used Python socket.connect_ex() to test port availability
- Configured common ports: 21, 22, 80, 443, 8080
- Added Poetry entry point for clean execution

## Why
- Understand service discovery at network level
- Avoid treating tools like Nmap as black boxes
- Practice building small security utilities as proper software
- Prepare for future CI/DevSecOps automation

## Example
poetry run portscan scanme.nmap.org

## Next
- Compare results with Nmap
- Containerize with Docker
- Integrate into CI pipeline (automated scan on commit)

