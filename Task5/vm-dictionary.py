vm = {
    "id": "vm-101",
    "ip": "10.0.0.5",
    "status": "running",
    "region": "eu-west-1"
}
vm["status"] = "stopped"

vm["instance_type"] = "t2.micro"

print(vm)
