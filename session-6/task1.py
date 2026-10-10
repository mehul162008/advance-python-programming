class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


user = User("mehul", "mehul@gmail.com")

print("Username:", user.username)
print("Email:", user.email)