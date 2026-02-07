# Day 6 – Security Automation (Tool Chaining)

## Built
- Bash automation script to chain multiple security tools
- Runs:
  1. portscan (service discovery)
  2. logscan (suspicious activity detection)

## Implementation
- Simple shell script orchestration
- Single command executes multiple checks
- Designed for repeatable execution

## Why
Running tools manually does not scale.
Automation ensures:
- consistency
- faster checks
- fewer manual steps

Shell chosen over Python since this is orchestration, not logic.

## Outcome
One command performs multiple security validations.

## Example
./scripts/security_check.sh scanme.nmap.org data/sample.log

## Next
Integrate these checks into CI/CD (DevSecOps pipeline).

