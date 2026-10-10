class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating


m = Movie("83", 4.5)

print(m.title, m.rating)