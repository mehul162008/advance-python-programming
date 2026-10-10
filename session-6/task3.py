class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge


user = VerifiedInfluencer("mehul", "mehul@gmail.com", 244, True)

print("Username:", user.username)
print("Email:", user.email)
print("Followers:", user.followers)
print("Badge:", user.badge)