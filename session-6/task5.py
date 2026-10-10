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

    def display_profile(self):
        if self.followers >= 1000000:
            followers = str(round(self.followers / 1000000, 1)) + "M"
        elif self.followers >= 1000:
            followers = str(round(self.followers / 1000, 1)) + "K"
        else:
            followers = str(self.followers)

        print("Username:", self.username)
        print("Followers:", followers)
        print("Verified Badge:", self.badge)


user = VerifiedInfluencer("mehul", "mehul@gmail.com", 15000, True)

user.display_profile()