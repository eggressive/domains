"""Attempts to resolve domains from file"""
import socket

data = open("domains.txt", "r") 

dns = data.read().splitlines()
print('For domain list: ')
print(dns)
print("\n")

for i in dns:
    try:
        ip = socket.gethostbyname(i)
        print(i + " resolves to " + ip)
    except Exception:
        print(i + " resolution failed")
