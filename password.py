import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle button click event
def generate_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Length must be greater than 0")
        else:
            password = generate_password(length)
            password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        password_label.config(text="Please enter a valid integer for length")

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Create label and entry for password length
length_label = tk.Label(window, text="Enter password length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_button_click)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create label to display generated password
password_label = tk.Label(window, text="", wraplength=300)
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
