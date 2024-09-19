import tkinter as tk
from tkinter import messagebox
import file1



def login():
    username = "digvijay"
    password = "12345"
    if entry_username.get() == username and entry_password.get() == password:    
        messagebox.showinfo(title="Login sucess" , message="you have succssfully loged in...")
        print("hello ,,welcome to network IDS")
    else:
        messagebox.showinfo(title="login failed" , message="Invalid credentials ")

        print("invalid username")
# Create the main window
window = tk.Tk()

# Create a frame with a purple background
frame1 = tk.Frame(window, bg='grey')

# Set the title and size of the window
window.title("Login Page")
window.geometry('1080x720')

# Create and place the label for the login page title
label1 = tk.Label(frame1, text="LOGIN PAGE", bg="grey", fg="white", font=('Arial', 30))
label1.grid(row=0, column=2, columnspan=2, sticky="news", padx=20, pady=20)

# Create and place the label for the username
label_username = tk.Label(frame1, text="UserName", bg="grey", fg="white", font=('Arial', 18))
label_username.grid(row=1, column=0, pady=20, padx=20)

# Create and place the label for the password
label_password = tk.Label(frame1, text="Password", bg="grey", fg="white", font=('Arial', 18))
label_password.grid(row=2, column=0, pady=15, padx=10)

# Create and place the entry widget for the username
entry_username = tk.Entry(frame1, font=('Arial', 18))
entry_username.grid(row=1, column=2, padx=10)

# Create and place the entry widget for the password
entry_password = tk.Entry(frame1, show="*", font=('Arial', 18))
entry_password.grid(row=2, column=2, padx=10)

# Create and place the login button
button1 = tk.Button(frame1, text="LOGIN", bg="pink", fg="white", font=('Arial', 18) , command= login)
button1.grid(row=3, column=2, columnspan=2, pady=15)
signupButton= tk.Button(frame1,text="sign up",bg="grey",fg="blue",command=file1.run_script)
signupButton.grid(row=3,column=3)

# Pack the frame
frame1.pack(pady=20, padx=20)

# Set the background color of the window
window.configure(bg="grey")

# Run the main loop
window.mainloop()

