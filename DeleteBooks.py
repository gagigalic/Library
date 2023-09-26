import sqlite3
import customtkinter
from tkinter import messagebox, FALSE

def destroy():
    app.destroy()


def delete_book():
    try:
        id = book_entry.get()
        conn = sqlite3.connect("Library.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id= ?",(id,))
        conn.commit()
        messagebox.showinfo("Succes", "The book was deleted")
        conn.close()


    except sqlite3.Error as e:
        print("Error", e)
        return False



def deleteBook():

    try:
        global book_entry, app

        app = customtkinter.CTk()
        app.title("Library")
        app.minsize(width=400, height=400)
        app.geometry("600x500")
        app.resizable(FALSE, FALSE)
        app.config(bg="#4682A9")

        font1 = ("Arial", 25, "bold")
        font2 = ("Arial", 20, "bold")

        return_title = customtkinter.CTkLabel(app, font=font1, text=" Delete Book", text_color="#fff", bg_color="#4682A9")
        return_title.place(x=200, y=80)

        book_id = customtkinter.CTkLabel(app, font=font2, text=" Book ID:", text_color="#fff", bg_color="#4682A9")
        book_id.place(x=120, y=250)

        book_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",
                                      border_width=2, width=180)
        book_entry.place(x=250, y=250)




        submit_button = customtkinter.CTkButton(app, command=delete_book, font=font2, text_color="#fff", text="SUBMIT",
                                            fg_color="#164B60", hover_color="#749BC2", bg_color="#4682A9",
                                            cursor="hand2",
                                            corner_radius=15, width=150)
        submit_button.place(x=80, y=430)

        quit_button = customtkinter.CTkButton(app,command = destroy, font=font2, text_color="#fff", text="Quit",
                                            fg_color="#164B60", hover_color="#749BC2", bg_color="#4682A9",
                                            cursor="hand2",
                                            corner_radius=15, width=150)
        quit_button.place(x=280, y=430)



        app.mainloop()
    except sqlite3.Error as e:
        print("Error", e)
        return False

