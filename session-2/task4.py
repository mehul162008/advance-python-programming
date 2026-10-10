file = open("lyrics.txt", "r")

file.readline()
file.readline()

third_song = file.readline()

print("Third song:", third_song.strip())

file.close()