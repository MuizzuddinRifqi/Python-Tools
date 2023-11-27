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

elif '-' in ports:
    portRange = ports.split('-')
    start = int(portRange[0])
    end = int(portRange[1])
    for port in range(start, end + 1):
        scan_port(target, port)

else:
    scan_port(target, int(ports))