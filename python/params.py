import requests
import random

url = "https://icanhazdadjoke.com/search"

user = input("LET ME TELL YOU A JOKE! Give me the topic now: ")

r = requests.get(url, 
	headers={"Accept": "application/json"},
	params={"term": user}

)

a = r.json()

number = (a["total_jokes"])

if number == 1:
	print("I just have One joke")

elif number == 0:
	print("NO JOKES")
else:
	print(f"I have {number} jokes for you, darling!\n")

b = random.choice(a["results"])
c = b["joke"]
print("\n"+c)

