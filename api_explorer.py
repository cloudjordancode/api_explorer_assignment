import requests


# GET ALL USERS : NAME/EMAIL
response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()

print(f"Status Code: {response.status_code}")
print(f"Number of users: {len(users)}")

for user in users:
    print(user["name"], user["email"])


# GET ALL POSTS by USER #3
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3}
)

posts = response.json()


print(f"Status Code: {response.status_code}")
print(f"Number of posts: {len(posts)}")

for post in posts:
    print(post)

# GET ALL COMMENTS ON POST #1
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1/comments",
)

comments = response.json()

print(f"Status Code: {response.status_code}")
print(f"Number of comments: {len(comments)}")

for comment in comments:
    print(comment)


new_post = {
    "title": "My First API Post",
    "body": "This was created by sending a POST request!",
    "userId": 1,
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

created = response.json()

print(f"\nCreate Status: {response.status_code}")
print(f"Created post with id: {created['id']}")
print(f"Title: {created['title']}")
print(created)