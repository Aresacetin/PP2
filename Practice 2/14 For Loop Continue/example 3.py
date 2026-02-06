# Listing only txt files in directory
files = ["notes.txt", "image.png", "password.txt", "Lecture01.pdf", "wasd.txt"]

for i in files:
    if not i.endswith(".txt"):
        continue
    print(i)
