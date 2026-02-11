import sys
from collections import Counter

THRESHOLD = 2


def parse_logs(filepath: str):
    failed_ips = []

    with open(filepath) as f:
        for line in f:
            if "401" in line or "403" in line:
                ip = line.split()[0]
                failed_ips.append(ip)

    counts = Counter(failed_ips)

    print("\nSuspicious IPs:\n")

    found = False
    for ip, count in counts.items():
        if count >= THRESHOLD:
            found = True

    print("\n=== Security Log Summary ===")
    if found:
        print(f"Suspicious IPs detected: {len(counts)}\n")
        for ip, count in counts.items():
            if count >= THRESHOLD:
                print(f"[ALERT] {ip} -> {count} failures")

        print("\nStatus: FAILED")
        sys.exit(1)

    else:
        print("No suspicious activity detected")
        print("Status: PASSED")
        sys.exit(0)


def main():
    if len(sys.argv) < 2:
        print("Usage: logscan <logfile>")
        sys.exit(1)

    parse_logs(sys.argv[1])


if __name__ == "__main__":
    main()

