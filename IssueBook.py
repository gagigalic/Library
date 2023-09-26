import sqlite3
import customtkinter
from tkinter import messagebox, FALSE

def close():
    app.destroy()


def change_status(id_issued):

    status_issued = "Issused"

    try:
        with sqlite3.connect("Library.db") as conn:
            cursor=conn.cursor()
            cursor.execute("UPDATE books SET status= ? WHERE id =?",
                           (status_issued, id_issued))
            conn.commit()
            conn.close()


    except sqlite3.Error as e:
        print("Error", e)
        return False

def issuedBook():

    id_issued =book_entry.get()
    issuedto = issued.get()

    try:

        with sqlite3.connect("Library.db") as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM books WHERE id=?", (id_issued))
            result = cursor.fetchone()

            if result is None:

                messagebox.showinfo("Message", f"Book does not exist in the Library")
            else:

                cursor.execute('INSERT or IGNORE INTO books_issued (id, issuedto) VALUES (?,?)',
                           (id_issued, issuedto))
                conn.commit()
                messagebox.showinfo("Succes","The book is issued")
                conn.close()

        change_status(id_issued)
    except sqlite3.Error as e:
        print("Error", e)
        return False



def issueBook():

    global issued, book_entry, app
    book_entry = None

    app = customtkinter.CTk()
    app.title("Library")
    app.minsize(width=400, height=400)
    app.geometry("600x500")
    app.resizable(FALSE, FALSE)
    app.config(bg="#4682A9")

    font1 = ("Arial", 25, "bold")
    font2 = ("Arial", 20, "bold")

    return_title = customtkinter.CTkLabel(app, font=font1, text=" Issue Book", text_color="#fff", bg_color="#4682A9")
    return_title.place(x=200, y=80)

    book_id = customtkinter.CTkLabel(app, font=font2, text=" Book ID:", text_color="#fff", bg_color="#4682A9")
    book_id.place(x=120, y=200)

    book_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",
                                      border_width=2, width=180)
    book_entry.place(x=250, y=200)

    book_id = customtkinter.CTkLabel(app, font=font2, text=" Issued To:", text_color="#fff", bg_color="#4682A9")
    book_id.place(x=120, y=250)

    issued = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",
                                        border_width=2, width=180)
    issued.place(x=250, y=250)




    issue_book = customtkinter.CTkButton(app, command =issuedBook,  font=font2, text_color="#fff", text="SUBMIT",
                                            fg_color="#164B60", hover_color="#749BC2", bg_color="#4682A9",
                                            cursor="hand2",
                                            corner_radius=15, width=150)
    issue_book.place(x=80, y=430)

    quit_button = customtkinter.CTkButton(app, command = close, font=font2, text_color="#fff", text="Quit",
                                            fg_color="#164B60", hover_color="#749BC2", bg_color="#4682A9",
                                            cursor="hand2",
                                            corner_radius=15, width=150)
    quit_button.place(x=280, y=430)



    app.mainloop()





