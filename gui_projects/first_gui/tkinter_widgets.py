import tkinter as tk  # Import Tkinter

# Function that runs when the button is clicked
def show_text():
    user_input = entry.get()  # Getting text from the user
    label.config(text=f"You entered: {user_input}")  # Displaying text inside the label

# Creating the main window
root = tk.Tk()
root.title("Tkinter Widgets")
root.geometry("800x1200")

# Creating graphical widgets
label = tk.Label(root, text="Enter something:", font=("Arial", 14))
label.pack(pady=10)  # Adding space between widgets

entry = tk.Entry(root, font=("Arial", 14))  # User input
entry.pack(pady=5)

button = tk.Button(root, text="Show Text", command=show_text)  # Button that displays the text
button.pack(pady=10)

# Running the program
root.mainloop()
