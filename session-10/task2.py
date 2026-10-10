import tkinter as tk

root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")

title = tk.Label(root, text="My Music Player", font=("Arial", 16))
title.pack(pady=15)

status = tk.Label(root, text="Select an action")
status.pack(pady=10)


def play():
    status.config(text="Playing")


def pause():
    status.config(text="Paused")


def next_song():
    status.config(text="Next Song")


tk.Button(root, text="Play", command=play).pack(pady=5)
tk.Button(root, text="Pause", command=pause).pack(pady=5)
tk.Button(root, text="Next", command=next_song).pack(pady=5)

root.mainloop()