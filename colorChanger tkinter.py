# pip install tkinter

import tkinter as tk
import random

colours = [
    'red', 'blue', 'green',
    'pink','black', 'yellow',
    'orange','white','purple',
    'brown'] 

# create a GUI Window
root = tk.Tk()

# set the size of the window
root.geometry("400x400")

# set the title
root.title("Color Changer")

# function to change the colour of window dynamically
def changeColor():
    # choosing random colours from the list
    k = random.choice(colours)
    root.configure(bg=k)


# to display text in a window
label = tk.Label(root, text="Color Changer in Tkinter", bg="white")
label.pack()

# using button to change the window color
button = tk.Button(text="Change", command=changeColor)
button.pack()

# close the window manually
quit_button = tk.Button(text="Quit", command=root.destroy)
quit_button.pack()

# start the GUI Window
root.mainloop()
