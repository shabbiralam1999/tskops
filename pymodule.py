import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.get(url)
    response.raise_for_status()
    post = response.json()
    print(f"Successfully fetch {post} posts.")
except requests.exceptions.RequestException as e:
    print(f"You have made a mistake.")