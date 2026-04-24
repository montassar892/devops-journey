import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
first_five = posts[:5]

with open("posts.json", "w") as f:
    json.dump(first_five, f, indent=2)

print(f"Done! Fetched {len(first_five)} posts")
print(f"Status code: {response.status_code}")
