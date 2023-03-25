import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False,False)

#To center window
w = 500  
h = 300 
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def browseFiles():
    fileTypes = (('text files', '*.txt*'), ('all files', '*.*'))
    fileName = fd.askopenfilename(title='Open a File', initialdir= '/', filetypes=fileTypes)
    showinfo(title='Selected File', message=fileName)

open_Button = ttk.Button(root, text='Open a File', command=browseFiles)
exit_Button = ttk.Button(root, text='Exit', command=exit)

open_Button.pack(expand = True)
exit_Button.pack(expand = True)

root.mainloop()
