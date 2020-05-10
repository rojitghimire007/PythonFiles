import requests

url = "https://icanhazdadjoke.com/"

r = requests.get(url, headers={"Accept": "application/json"})

print(r.text)
a = r.json()

print(a["joke"])
print(a["status"])