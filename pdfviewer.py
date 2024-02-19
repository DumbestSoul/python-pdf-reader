from tkinter import *   # importing everything from tkinter
from tkinter import ttk # import ttk module for styling widgets
from tkinter import filedialog as fd
import os


# PDF viewer class
class PDFViewer:
    def __init__(self, master):
        # THIS ALL VARAIBLE IS FOR THE CURRENT PDF FILE
        self.path = None
        self.fileisopen = None
        self.author = None
        self.name = None
        self.curr_page = 0
        self.numPages = None
        self.master = master
        self.master.title('PDF VIEWER')
        self.master.geometry('580x520+440+180')
        self.master.resizable(width=0, height=0)
        self.master.iconbitmap(self.master, 'pdf_file_icon.ico')
        # CREATING THE MENU SYSTEM
        self.menu = Menu(self.master)   # creating the menu
        self.master.config(menu=self.menu)  # adding it to the main window
        self.filemenu = Menu(self.menu) # creating a sub menu
        self.menu.add_cascade(label="File", menu=self.filemenu) # adding a level to sub-menu
        self.filemenu.add_command(label="Open File")
        self.filemenu.add_command(label="Exit")


root = Tk()

app = PDFViewer(root)

root.mainloop()



