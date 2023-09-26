from AddBook import *
from DeleteBooks import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

app = customtkinter.CTk()
app.title("Library")
app.minsize(width=400, height=400)
app.geometry("600x500")
app.resizable(FALSE, FALSE)
app.config(bg = "#4682A9")

font1= ("Arial", 25, "bold")
font2 = ("Arial", 20, "bold")

id_label = customtkinter.CTkLabel(app, font=font1, text = "Welcome to Library", text_color= "#fff", bg_color="#4682A9")
id_label.place(x=180, y=100)

add_button = customtkinter.CTkButton(app, command = addBook, font = font2, text_color="#fff", text = "Add Book details", fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor ="hand2", corner_radius=15, width=200)
add_button.place(x=180, y=180)

delete_book = customtkinter.CTkButton(app,command=deleteBook, font = font2, text_color="#fff", text = "Delete Book", fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor ="hand2", corner_radius=15, width=200)
delete_book.place(x=180, y=230)

view_book = customtkinter.CTkButton(app, command=View, font = font2, text_color="#fff", text = "View Book List", fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor ="hand2", corner_radius=15, width=200)
view_book.place(x=180, y=280)

issue_book = customtkinter.CTkButton(app, command=issueBook, font = font2, text_color="#fff", text = "Issue Book", fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor ="hand2", corner_radius=15, width=200)
issue_book.place(x=180, y=320)

return_book = customtkinter.CTkButton(app, command = returnBook, font = font2, text_color="#fff", text = "Return Book", fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor ="hand2", corner_radius=15, width=200)
return_book.place(x=180, y=370)

app.mainloop()