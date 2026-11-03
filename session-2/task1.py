file = open("lyrics.txt", "r")

print(file.tell())

data = file.read(10)

print(data)
print(file.tell())

file.close()