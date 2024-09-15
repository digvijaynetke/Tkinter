import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('300x200')

# Create a style
style = ttk.Style()

# Configure a custom style for the LabelFrame
style.configure('Custom.TLabelframe', background='lightblue')  # LabelFrame background
style.configure('Custom.TLabelframe.Label', foreground='blue')  # LabelFrame label color

# Create a LabelFrame using the custom style
label_frame = ttk.LabelFrame(root, text="Custom LabelFrame", style='Custom.TLabelframe')
label_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Add a widget inside the LabelFrame
label = ttk.Label(label_frame, text="Content inside LabelFrame")
label.pack(padx=20, pady=20)

# Start the application
root.mainloop()
