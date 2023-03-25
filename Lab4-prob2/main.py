import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False,False)
root.geometry("300x150")

def browseFiles():
    fileTypes = (('text files', '*.txt*'), ('all files', '*.*'))
    fileName = fd.askopenfilename(title='Open a File', initialdir= '/', filetypes=fileTypes)
    showinfo(title='Selected File', message=fileName)

open_Button = ttk.Button(root, text='Open a File', command=browseFiles)

open_Button.pack(expand = True)

root.mainloop()