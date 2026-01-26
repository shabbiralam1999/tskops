port = int(input("ENter Your Port: "))
for i in range(1,65536):
    if i <= port:
        print(f'Your port {port} is valid')
        break
    else:
        print(f"Your port is invalid")