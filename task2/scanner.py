DANGEROUS_PORTS = (21, 23, 445)
def check_ports(active_ports):
    for port in active_ports:
        if port in DANGEROUS_PORTS:
            print(f'Your {port} port is dangerous.')
        else:
            print(f'Your {port} port is safe.')