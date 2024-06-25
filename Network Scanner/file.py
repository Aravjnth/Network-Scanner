import socket

def scan_host(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

target_host = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

open_ports = scan_host(target_host, start_port, end_port)

if open_ports:
    print(f"Open ports on {target_host} are: {open_ports}")
else:
    print(f"No open ports found on {target_host} within the range {start_port}-{end_port}.")