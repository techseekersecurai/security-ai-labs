import socket
import sys


def scan(target, ports):
	print(f"Scanning {target}\n")

	for port in ports:
		s = socket.socket()
		s.settimeout(1)
		result = s.connect_ex((target,port))

		if result == 0:
			print(f"[OPEN]  {port}")
		else:
			print(f"[CLOSED]  {port}")

		s.close()

def main():
	if len(sys.argv) < 2:
		print("Usage: portscan <host>")
		return

	host = sys.argv[1]
	ports = [21, 22, 80, 443, 8080]
	scan(host, ports)
