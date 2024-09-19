import tkinter as tk
from tkinter import messagebox
import second

def confirm_information():
    # Retrieve user inputs
    firstname = second.first_name_entry.get()
    lastname = second.last_name_entry.get()
    age = second.age_spinbox.get()
    nationality = second.nationality_combobox.get()
    numCourses = second.numcourse_spinbox.get()
    registration_status = second.registration_check.get()

    # Create the message to display for confirmation
    confirmation_message = f"""
    Please confirm your details:
    
    First Name: {firstname}
    Last Name: {lastname}
    Age: {age}
    Nationality: {nationality}
    Number of Courses: {numCourses}
    Registration Status: {"Registered" if registration_status == 1 else "Not Registered"}
    """
    
    # Show the confirmation dialog
    if messagebox.askyesno("Confirm Information", confirmation_message):
        # If user confirms, store data to the database (or further process)
        messagebox.showinfo("Success", "Your information has been stored successfully.")
    else:
        # If user declines, notify them
        messagebox.showwarning("Cancelled", "Information submission was cancelled.")

# Sample UI setup
second = tk.Tk()  # This would be your second window where input is taken

# Sample widgets for demonstration purposes
second.first_name_entry = tk.Entry(second)
second.last_name_entry = tk.Entry(second)
second.age_spinbox = tk.Spinbox(second, from_=0, to=120)
second.nationality_combobox = tk.Entry(second)  # Normally, you'd use a Combobox widget here
second.numcourse_spinbox = tk.Spinbox(second, from_=0, to=10)
second.registration_check = tk.IntVar()
checkbutton = tk.Checkbutton(second, text="Registration Status", variable=second.registration_check)

# Place widgets (this would be your layout)
second.first_name_entry.pack()
second.last_name_entry.pack()
second.age_spinbox.pack()
second.nationality_combobox.pack()
second.numcourse_spinbox.pack()
checkbutton.pack()

# Button to trigger confirmation dialog
confirm_button = tk.Button(second, text="Confirm", command=confirm_information)
confirm_button.pack()

second.mainloop()
