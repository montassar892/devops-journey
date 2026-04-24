import requests
import json

# 1. Call the API
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# 2. Convert to JSON
posts = response.json()

# 3. Take only the first 5 posts
first_five = posts[:5]

# 4. Save them to a file
with open("posts.json", "w") as f:
    json.dump(first_five, f, indent=2)

print(f"Done! Saved {len(first_five)} posts to posts.json")
print(f"Status code: {response.status_code}")








