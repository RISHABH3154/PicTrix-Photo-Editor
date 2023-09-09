import tkinter as tk

root = tk.Tk()

# Configure the button style
style = tk.Style()
style.configure("TButton", font=("Helvetica", 14), foreground="white", background="#4CAF50", bd=0, activebackground="#3e8e41")

# Create a button with the configured style
button = tk.Button(root, text="Click me!", style="TButton")

# Pack the button into the window
button.pack(padx=20, pady=20)

root.mainloop()
