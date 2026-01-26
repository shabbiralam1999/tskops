import json
mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'
def process_server_data(json_string):
    try:
        data = json.loads(json_string)
        servers = data.get("servers",[])
        for server in servers:
            name = server.get("name")
            status = server.get("status")
            print(f'Server {name} is {status}.')
    except json.JSONDecodeError as e:
        print("Json data is invalid.")
        print(e)
process_server_data(mock_api)    
