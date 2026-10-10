import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("350x250")


tk.Label(root, text="Username").pack(pady=5)
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack(pady=5)
password = tk.Entry(root, show="*")
password.pack()

message = tk.Label(root, text="")
message.pack(pady=10)


def login():
    if username.get() != "" and password.get() != "":
        message.config(text="Login Successful")
    else:
        message.config(text="Please fill both fields")


tk.Button(root, text="Login", command=login).pack(pady=5)

root.mainloop()