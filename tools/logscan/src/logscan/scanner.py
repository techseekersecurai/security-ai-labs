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
            print(f"{ip} -> {count} failures")
            found = True

    if not found:
        print("No suspicious activity found.")


def main():
    if len(sys.argv) < 2:
        print("Usage: logscan <logfile>")
        sys.exit(1)

    parse_logs(sys.argv[1])


if __name__ == "__main__":
    main()

