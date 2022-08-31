from cgitb import text
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from idlelib.tooltip import Hovertip

window = Tk()
window.title("Book Information Store")
window.iconphoto(False, PhotoImage(file='images/icon.png'))
window.minsize(1300,700)
window.configure(bg='lightblue')


icon_image = Image.open("images/icon.png")
book_photo = ImageTk.PhotoImage(icon_image)
book_label = Label(image=book_photo, bg='lightblue')
book_label.place(x=600, y=15)

info_frame = LabelFrame(window, text="Book Information", relief=RIDGE, bg='#a9c0e2', font=('arial', 15, 'bold'), fg='black')
info_frame.place(x=10, y=10, width=460, height=110)


title_label = Label(info_frame, text='Title', font=('arial', 12, 'bold'), bg='#a9c0e2', fg='black')
title_label.grid(row=0, column=0, padx=5, pady=5)
title_text = StringVar()
title_entry = Entry(info_frame, textvariable=title_text)
title_entry.grid(row=0, column=1, padx=5, pady=5)

year_label = Label(info_frame,text="Year", font=('arial', 12, 'bold'), bg='#a9c0e2', fg='black')
year_label.grid(row=1, column=0, padx=5, pady=5)
year_text = IntVar(value=1900)
year_entry = Entry(info_frame, textvariable=year_text)
year_entry.grid(row=1, column=1, padx=5, pady=5)


author_label = Label(info_frame, text="Author", font=('arial', 12, 'bold'), bg='#a9c0e2', fg='black')
author_label.grid(row=0, column=3, padx=5, pady=5)
author_text = StringVar()
author_entry = Entry(info_frame, textvariable=author_text)
author_entry.grid(row=0, column=4, padx=5, pady=5)

publisher_label = Label(info_frame, text="Publisher", font=('arial', 12, 'bold'), bg='#a9c0e2', fg='black')
publisher_label.grid(row=1, column=3, padx=5, pady=5)
publisher_text = StringVar()
publisher_entry = Entry(info_frame, textvariable=publisher_text)
publisher_entry.grid(row=1, column=4, padx=5, pady=5)


list = Listbox(window, height=10, width=35)
list.place(x=10, y=130, height=560, width=1280)


tools_frame = LabelFrame(window, text="Tools", relief=RIDGE, bg='#a9c0e2', font=('arial', 15, 'bold'), fg='black')
tools_frame.place(x=830, y=10, width=460, height=110)

view_image = PhotoImage(file='images/view_all.png', height=50, width=50)
view_btn = Button(tools_frame, image=view_image, bg='#a9c0e2', fg='black')
view_btn_hover = Hovertip(view_btn, 'View All', hover_delay=10)
view_btn.grid(row=0, column=0, padx=15, pady=5)

search_image = PhotoImage(file='images/search.png', height=50, width=50)
search_btn = Button(tools_frame, image=search_image, bg='#a9c0e2', fg='black')
search_btn_hover = Hovertip(search_btn, 'Search Entry', hover_delay=10)
search_btn.grid(row=0, column=1, pady=5)

add_image = PhotoImage(file='images/add.png', height=50, width=50)
add_btn = Button(tools_frame, image=add_image, bg='#a9c0e2', fg='black')
add_btn_hover = Hovertip(add_btn, 'Add Entry', hover_delay=10)
add_btn.grid(row=0, column=2, padx=10, pady=5)

update_image = PhotoImage(file='images/update.png', height=50, width=50)
update_btn = Button(tools_frame, image=update_image, bg='#a9c0e2', fg='black')
update_btn_hover = Hovertip(update_btn, 'Update', hover_delay=10)
update_btn.grid(row=0, column=3, padx=10, pady=5)

delete_image = PhotoImage(file='images/delete.png', height=50, width=50)
delete_btn = Button(tools_frame, image=delete_image, bg='#a9c0e2', fg='black')
delete_btn_hover = Hovertip(delete_btn, 'Delete', hover_delay=10)
delete_btn.grid(row=0, column=4, padx=10, pady=5)

close_image = PhotoImage(file='images/close.png', height=50, width=50)
close_btn = Button(tools_frame, image=close_image, bg='#a9c0e2', fg='black')
close_btn_hover = Hovertip(close_btn, 'Close', hover_delay=10)
close_btn.grid(row=0, column=5, padx=10, pady=5)

window.mainloop()