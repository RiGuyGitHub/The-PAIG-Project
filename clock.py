import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)

# Set up the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg="black")

# Create a label for displaying the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the update_time function to initialize the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
