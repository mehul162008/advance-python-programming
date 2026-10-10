import random
from songs import song_list

random.shuffle(song_list)

print("Shuffled Playlist:")

for song in song_list:
    print(song)