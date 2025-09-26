import requests

response = requests.post("http://localhost:5000", json={
    "jsonrpc": "2.0", 
    "method": "create_user", 
    "params": ["Joao Silva", "joao@email.com", 30], 
    "id": 1
})
print("CREATE:", response.text)

response = requests.post("http://localhost:5000", json={
    "jsonrpc": "2.0", 
    "method": "list_users", 
    "params": [], 
    "id": 2
})
print("READ (List):", response.text)

response = requests.post("http://localhost:5000", json={
    "jsonrpc": "2.0", 
    "method": "get_user", 
    "params": [1], 
    "id": 3
})
print("READ (Get):", response.text)

response = requests.post("http://localhost:5000", json={
    "jsonrpc": "2.0", 
    "method": "update_user", 
    "params": [1, "Joao Pedro", "joao@email.com", 31], 
    "id": 4
})
print("UPDATE:", response.text)


response = requests.post("http://localhost:5000", json={
    "jsonrpc": "2.0", 
    "method": "delete_user", 
    "params": [1], 
    "id": 5
})
print("DELETE:", response.text)