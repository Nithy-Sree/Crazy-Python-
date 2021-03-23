# install the necessary packages
# pip install PyDictionary
# pip install tkinter

import tkinter as tk
from PyDictionary import PyDictionary
from tkinter import messagebox

root = tk.Tk()
root.title("Dictionary in Python!")
root.geometry("400x300")

# to find the meaning of the word
def mean():
    word = f"{base.get()}"
    meani = PyDictionary.meaning("word")
    messagebox.showinfo("Success", meani)
		

# to erase the entry
def clear():
    entry.delete(0, tk.END)


# to find the opposite of the entered word
def ant():
    word = f"{base.get()}"
    anto = PyDictionary.antonym("word")
    messagebox.showinfo("Success", anto)

# to find the meaning of the entered word
def syn():
    word = f"{base.get()}"
    syno = PyDictionary.meaning("word")
    messagebox.showinfo("Success", syno)

# used to implement display boxes to place text
label = tk.Label(root, text="Enter the Word: ")
label.grid(row=0, column=0, padx=8, pady=8)	
# label.pack()

# used to store the entered data in the entry
base = tk.StringVar()

# for entering the word
entry = tk.Entry(root, textvariable=base)
entry.grid(row=0, column=1)

# button to find the meaning 
mean = tk.Button(root, text="MEANING", command = mean)
mean.grid(row=1, column=0, padx=8, pady=8)

# button to find the synonym
syno = tk.Button(root, text="SYNONYM", command = syn)
syno.grid(row=1, column=1, padx=8, pady=8)

# button to find the antonym 
anto = tk.Button(root, text="ANTONYM", command = ant)
anto.grid(row=1, column=2, padx=8, pady=8)


# to clear the text field for entering another word
buttonclear = tk.Button(root, text="CLEAR", command=clear)
buttonclear.grid(row=2, column=0, padx=8, pady=8)

# to stop the process
buttonquit = tk.Button(root, text="QUIT", command=root.destroy)
buttonquit.grid(row=2, column=1, padx=8, pady=8)

# to start a window
root.mainloop()
