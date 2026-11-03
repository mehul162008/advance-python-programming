file = open("my_fav_songs.txt", "r")

count = 1

for song in file:
    print(count, song.strip())
    count += 1

file.close()