# Create playlist.txt
file = open("playlist.txt", "w")

file.write("Kesariya\n")
file.write("Heeriye\n")
file.write("Apna Bana Le\n")
file.write("Tum Hi Ho\n")
file.write("Chogada\n")

file.close()


# Read only the third song
file = open("playlist.txt", "r")

file.readline()
file.readline()

print("Third Song:", file.readline().strip())

file.close()