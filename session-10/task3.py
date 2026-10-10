import tkinter as tk

root = tk.Tk()
root.title("Music Options")
root.geometry("350x200")

tk.Button(root, text="Like").grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Share").grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Download").grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="Add to Queue").grid(row=1, column=1, padx=10, pady=10)

root.mainloop()