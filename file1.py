import subprocess
import utils
import tkinter as tk
from tkinter import messagebox

def run_script():
    subprocess.run(['python','second.py'])

def enter_data():
 
    # firstname = second.first_name_entry.get()
    # lastname = second.last_name_entry.get()
    # age = second.age_spinbox.get()
    # nationality = second.nationality_combobox.get()
    # numCourses = second.numcourse_spinbox.get()

    firstname = utils.get_firstname()  # Access from utils.py
    lastname = utils.get_lastname()
    age = utils.get_age()
    nationality = utils.get_nationality()
    numCourses = utils.get_numCourses()

    # registration_status = second.registration_check.get()
    messagebox.showinfo(title="Verification",message=f"""
    Please confirm your details:
    
    First Name: {firstname}
    Last Name: {lastname}
    Age: {age}
    Nationality: {nationality}
    Number of Courses: {numCourses}
     """)
    return
    