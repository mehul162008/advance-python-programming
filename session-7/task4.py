class Content:
    def display(self, title):
        print("Title:", title)


class Movie(Content):
    def display(self, title, year):
        print("Title:", title)
        print("Year:", year)


movie = Movie()

movie.display("83", 2023)