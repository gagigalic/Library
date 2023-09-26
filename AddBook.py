import sqlite3
import customtkinter
from tkinter import messagebox


def bookRegister():

        id = id_entry.get()
        title= title_entry.get()
        author= author_entry.get()
        status =status_entry.get()

        try:
            with sqlite3.connect("Library.db") as conn:
                 cursor = conn.cursor()
                 cursor.execute('INSERT or IGNORE INTO books (id, title, author, status) VALUES (?,?,?,?)',
                            (id, title, author, status))
            conn.commit()
            messagebox.showinfo("Succes", "Book added successfully")
            conn.close()
            app.destroy()
        except sqlite3.Error as e:
            print("Error", e)
            return False

def addBook():

    try:

        global app,id_entry, title_entry, author_entry, status_entry, conn, cursor, name



        app = customtkinter.CTk()
        app.title("Library")
        app.minsize(width=400, height=400)
        app.geometry("600x500")
        app.resizable(False, False)
        app.config(bg="#4682A9")

        font1 = ("Arial", 25, "bold")
        font2 = ("Arial", 20, "bold")

        add_title = customtkinter.CTkLabel(app, font=font1, text=" Add Books", text_color="#fff", bg_color="#4682A9")
        add_title.place(x=180, y=100)

        id_label = customtkinter.CTkLabel(app, font=font2, text=" Book ID:", text_color="#fff", bg_color="#4682A9")
        id_label.place(x=120, y=180)

        id_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",border_width=2, width=180)
        id_entry.place(x=250, y=180)


        title_label = customtkinter.CTkLabel(app, font=font2, text=" Title:", text_color="#fff", bg_color="#4682A9")
        title_label.place(x=120, y=240)

        title_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",border_width=2, width=180)
        title_entry.place(x=250, y=240)

        author_label = customtkinter.CTkLabel(app, font=font2, text=" Author:", text_color="#fff", bg_color="#4682A9")
        author_label.place(x=120, y=300)

        author_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",border_width=2, width=180)
        author_entry.place(x=250, y=300)

        status_label = customtkinter.CTkLabel(app, font=font2, text="Status:", text_color="#fff", bg_color="#4682A9")
        status_label.place(x=120, y=360)

        status_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",border_width=2, width=180)
        status_entry.place(x=250, y=360)


        submit_button = customtkinter.CTkButton(app, command= bookRegister,  font=font2, text_color="#fff", text="SUBMIT",
                                             fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor="hand2",
                                             corner_radius=15, width=150)
        submit_button.place(x=80, y=430)

        quit_button = customtkinter.CTkButton(app, command=app.destroy, font=font2, text_color="#fff", text="Quit",
                                                fg_color="#164B60", hover_color="#749BC2", bg_color="#4682A9",
                                                cursor="hand2",
                                                corner_radius=15, width=150)
        quit_button.place(x=280, y=430)



        app.mainloop()
    except sqlite3.Error as e:
        print("Error", e)
        return False


