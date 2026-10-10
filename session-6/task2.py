class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


influencer = Influencer("mehul", "mehul@gmail.com", 244)

print("Username:", influencer.username)
print("Email:", influencer.email)
print("Followers:", influencer.followers)