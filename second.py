import tkinter as tk

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack()

window.title("Login Page")
window.geometry('1080x720')

# Use LabelFrame for a frame with a title
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

window.mainloop()
