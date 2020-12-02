# pip install validators
# pip install tkinter

# import the neccessary packages

import tkinter as tk
import validators
from tkinter import messagebox


# create a GUI window
root = tk.Tk()

# setting the title for the window
root.title("URL Validator")

# setting the size of the window to display
root.geometry("250x100")

def checkUrl():
    # to get the entered data in the Entry field
    urlEntry = f'{baseString.get()}'

    # print(url)
    if len(urlEntry) == 0:
        messagebox.showerror("Error!", "Enter a valid string")
    elif validators.url(urlEntry):
        messagebox.showinfo("Success", "URL you entered is Valid")
    else:
        messagebox.showwarning("Invalid", "URL is not Valid")
    

# displaying text in the window
label = tk.Label(root, text = "Enter URL to check (with http or https)")
label.pack()

# to hold a string value
baseString = tk.StringVar()

# getting input from the user using Entry
entry = tk.Entry(root, textvariable=baseString)
entry.pack()

# checking the entered string is valid url or not
validateButton = tk.Button(text="Check", command = checkUrl)
validateButton.pack()

# start the GUI Window
root.mainloop()
