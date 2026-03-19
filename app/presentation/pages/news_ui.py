import requests
response = requests.get("http://localhost:8000/test-news") # Chama o FastAPI
data = response.json()
print(data)