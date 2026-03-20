import requests
response = requests.get("http://api:8000/test-news")
data = response.json()
print(data)