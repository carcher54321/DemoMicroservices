import json
import requests

with open('data/medical_data.json', 'r') as file:
    data = json.load(file)

response = requests.request('POST', 'http://localhost:5000/api/operation/process', data=data)
print(response)
