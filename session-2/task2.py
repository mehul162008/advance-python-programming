file = open("lyrics.txt", "r")

file.seek(20)

print(file.tell())

data = file.readline()

print(data)

file.close()