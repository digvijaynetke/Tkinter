import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack()

window.title("Login Page")
window.geometry('1080x720')


user_info_frame = tk.LabelFrame(frame, text="User Information", bg="grey", fg="white")
user_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky="news")

first_name_label = tk.Label(user_info_frame , text = "First Name" , bg = "grey" , fg = "white")
first_name_label.grid(row = 0 , column=0)
last_name_label = tk.Label(user_info_frame , text = "Last Name" ,  bg = "grey", fg = "white")
last_name_label.grid(row = 1 , column= 0)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row = 0 , column= 1)
last_name_entry.grid(row=1 , column= 1)

#title_label = tk.Label(user_info_frame, text="Title", bg = "grey" , fg = "white")
title_combobox = ttk.Combobox(user_info_frame, values=[" ", "Mr", "Mrs", "Miss"])
#title_label.grid(row=0, column=2 )#padx=5, pady=5, sticky="W")
title_combobox.grid(row=1, column=2, sticky="W")#, padx=5, pady=5)

age_label = tk.Label(user_info_frame,text="AGE")
age_spinbox = tk.Spinbox(user_info_frame,from_== 18, to=90)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tk.Label

window.mainloop()
