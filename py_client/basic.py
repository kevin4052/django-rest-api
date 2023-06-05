import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={"abc": 123}, json={"title": "Abc123", "content": "Hello world", "price": "abc134"})

print(response.json())


