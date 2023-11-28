import socket
from termcolor import colored

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))

        service_version = sock.recv(1024)
        service_version = service_version.decode('utf-8')
        service_version = service_version.strip('\n')
        portstate = f'Port {str(port)}    open'
        print(colored(portstate, 'green'), end ='      ')
        print(f'{service_version}')
        
    except ConnectionRefusedError:
        print(colored(f'Port {str(port)}    closed', 'red'))
    except UnicodeDecodeError:
        print(colored(f'Port {str(port)}    open', 'green'))

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