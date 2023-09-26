import sqlite3
import customtkinter
from tkinter import messagebox, FALSE, END
from tkinter import ttk
import tkinter as tk
import Database


conn = sqlite3.connect("Library.db")
cursor = conn.cursor()

def add_to_treeview():
    books=Database.fetch_books()
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert("", END, values = book)


def close():
    app.destroy()


def View():
    global tree, app

    app = customtkinter.CTk()
    app.title("Library")
    app.minsize(width=400, height=400)
    app.geometry("600x500")
    app.resizable(FALSE, FALSE)
    app.config(bg="#4682A9")

    font1 = ("Arial", 25, "bold")
    font2 = ("Arial", 15, "bold")

    add_title = customtkinter.CTkLabel(app, font=font1, text=" View Books", text_color="#fff", bg_color="#4682A9")
    add_title.place(x=200, y=50)

    quit_button = customtkinter.CTkButton(app, command =close, font=font2, text_color="#fff", text="Quit",
                                          fg_color="#164B60", hover_color="#749BC2", bg_color="#4682A9",
                                          cursor="hand2",
                                          corner_radius=15, width=150)
    quit_button.place(x=200, y=430)

    style = ttk.Style(app)

    style.theme_use("clam")
    style.configure("Treeview", font=font2, foreground="#fff", background="#000", fieldbackground="#164B60")
    style.map("Treeview", background=[("selected", "#7C9D96")])
    tree = ttk.Treeview(app, height=15)


    tree["columns"] = ("ID", "Title", "Author", "Status")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("ID", anchor=tk.CENTER, width=120)
    tree.column("Title", anchor=tk.CENTER, width=120)
    tree.column("Author", anchor=tk.CENTER, width=120)
    tree.column("Status", anchor=tk.CENTER, width=120)

    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Status", text="Status")

    tree.place(x=120, y=180)

    tree.bind("<ButtonRelease>")
    add_to_treeview()


    app.mainloop()





