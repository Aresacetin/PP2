# Managing access to admin panel
users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "guest"},
    {"name": "Charlie", "role": "admin"}
]

for user in users:
    if user["role"] != "admin":
        continue
    print(f"Access to admin panel granted to admin {user['name']}")
