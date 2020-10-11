import requests
import json

# McSkidy needs to access the next page at /f(which is the value received
# from the data above) and keep track of the value at each step(in this case 's').
# McSkidy needs to do this until the 'value' and 'next' data have the value equal to 'end'.

URL = "http://10.10.169.100:3000"
new_url = "http://10.10.169.100:3000/{}"
flag = ""

response = requests.get(URL)
print(response.json()['next'])
while response.json()['next'] != 'end':
    flag += response.json()['value']
    response = requests.get(new_url.format(response.json()['next']))

print(flag)
