# Day 5 – Log Parsing Tool (Automation)

## Built
- CLI-based log parsing utility packaged with Poetry
- Command: logscan <logfile>
- Detects repeated failed requests (401/403)
- Threshold-based filtering to highlight suspicious IPs

## Implementation
- Parsed raw log lines
- Extracted source IPs
- Counted failures using collections.Counter
- Reported only IPs exceeding threshold

## Validation
- Tested with medium-sized sample logs
- Successfully identified repeated login/admin failures
- Output is concise and actionable

## Why
Manual log review does not scale.
Small automation tools provide faster visibility into suspicious activity and fit naturally into CI/DevSecOps workflows.

## Outcome
- First practical security automation tool
- Reusable CLI instead of one-off script
- Foundation for IDS-style detection and future AI log analysis

## Example
poetry run logscan data/sample.log

## Next
Chain tools together and automate routine checks.

