from cgitb import text
from tkinter import *
import tkinter
from PIL import ImageTk, Image

window = Tk()
window.iconphoto(False, PhotoImage(file='images/icon.png'))
window.minsize(1300,700)
window.configure(bg='lightblue')


icon_image = Image.open("images/icon.png")
book_photo = ImageTk.PhotoImage(icon_image)
book_label = Label(image=book_photo, bg='lightblue')
book_label.place(x=600, y=10)

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

window.mainloop()