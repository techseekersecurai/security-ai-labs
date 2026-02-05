import socket
import sys

# Small practical set (like real-world quick scans)
DEFAULT_PORTS = [
    21,    # ftp
    22,    # ssh
    25,    # smtp
    53,    # dns
    80,    # http
    110,   # pop3
    143,   # imap
    443,   # https
    445,   # smb
    3306,  # mysql
    5432,  # postgres
    6379,  # redis
    8080   # alt http
]

DEFAULT_TIMEOUT = 1.0


def scan(target: str, ports: list[int], timeout: float):
    print(f"\nScanning {target} (timeout={timeout}s)\n")

    open_ports = []

    for port in ports:
        sock = socket.socket()
        sock.settimeout(timeout)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    if not open_ports:
        print("No open ports found.")
    else:
        print("Open ports:")
        for p in open_ports:
            print(f"  {p}")


def main():
    if len(sys.argv) < 2:
        print("Usage: portscan <host> [timeout]")
        sys.exit(1)

    host = sys.argv[1]

    timeout = float(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_TIMEOUT

    scan(host, DEFAULT_PORTS, timeout)


if __name__ == "__main__":
    main()

