from tkinter import *
from tkinter import messagebox


def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "GROUP3" and password == "12345":

        root.destroy()

        import dashboard

    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )


def forgot_password():

    messagebox.showinfo(
        "Forgot Password",
        "Default Login\n\nUsername: admin\nPassword: 1234"
    )


root = Tk()

root.title("Login")
root.geometry("400x250")

Label(
    root,
    text="Student Records System",
    font=("Arial", 16)
).pack(pady=100)

Label(root, text="Username").pack()

username_entry = Entry(root)
username_entry.pack()

Label(root, text="Password").pack()

password_entry = Entry(root, show="*")
password_entry.pack()

Button(
    root,
    text="Login",
    command=login
).pack(pady=100)

Button(
    root,
    text="Forgot Password",
    command=forgot_password
).pack()

root.mainloop()