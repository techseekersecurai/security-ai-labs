# Day 4 – Validation & Refinement

## Validation
Compared custom port scanner results with Nmap.

Observations:
- Detected the same commonly open ports
- Nmap performs deeper checks (service/version detection)
- Custom tool is faster due to lightweight TCP connect approach

Conclusion:
- Useful for quick checks and automation
- Not intended to replace full scanners like Nmap

## Improvements
- Show only open ports (reduced noise)
- Added configurable timeout parameter
- Optimized for faster feedback

## Why
Small, focused tools integrate better with CI/CD and DevSecOps pipelines.
Goal is speed and simplicity over exhaustive scanning.

## Example
poetry run portscan scanme.nmap.org
poetry run portscan scanme.nmap.org 0.3

## Next
Move to log parsing and basic security automation.

