import socket

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print(f"Port {str(port)} is open")
    except ConnectionRefusedError:
        print(f'Port {str(port)} is closed')

target = input('[+] Target IP: ')
ports = (input('[+] Port: '))

if ',' in ports:
    portlist = ports.split(',')
    for port in portlist:
        scan_port(target, int(port))
else:
    scan_port(target, int(ports))