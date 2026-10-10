class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


song1 = Song("Vhalam Aavo Ne", "Gaman Santhal", 250)
song2 = Song("Moj Ma Revu", "Gaman Santhal", 225)

print(song1.title, song1.artist, song1.duration)
print(song2.title, song2.artist, song2.duration)