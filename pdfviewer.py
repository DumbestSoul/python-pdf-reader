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
        # creating the top frame
        self.top_frame = ttk.Frame(self.master, width=580, height=460)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.grid_propagate(False)    # The frame will not propagate
        self.bottom_frame=ttk.Frame(self.master, width=580, height=50)
        self.bottom_frame.grid(row=1, column=0)
        self.bottom_frame.grid_propagate(False)
        # creating vertical scollbar
        self.scrolly = Scrollbar(self.top_frame, orient=VERTICAL)
        self.scrolly.grid(row=0, column=1, sticky=(N, S))   # N=NORTH, S=SOUTH
        # creating horizontal scrollbar
        self.scrollx = Scrollbar(self.top_frame, orient=HORIZONTAL)
        self.scrollx.grid(row=1, column=0, sticky=(W, E))   #W=WEST, E=EAST
        # adding canvas
        self.output = Canvas(self.top_frame, bg='#ECE8F3', width=560, height=435)
        self.output.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        # adding the canvas
        self.output.grid(row=0, column=0)
        self.scrolly.configure(command=self.output.yview)
        self.scrollx.configure(command=self.output.xview)
        self.scrollx.configure(command=self.output.xview)
        # ADDING UP AND DOWN BUTTONS
        self.uparrow_icon=PhotoImage(file='uparrow.png')
        self.downarrow_icon=PhotoImage(file='downarrow.png')
        self.uparrow=self.uparrow_icon.subsample(5, 5)
        self.downarrow=self.downarrow_icon.subsample(5, 5)
        self.upbutton = ttk.Button(self.bottom_frame, image=self.uparrow)
        self.upbutton.grid(row=0, column=1, padx=(270, 5), pady=8)
        self.downbutton = ttk.Button(self.bottom_frame, image=self.downarrow)
        self.downbutton.grid(row=0, column=3, pady=8)
        self.page_label = ttk.Label(self.bottom_frame, text='page')
        self.page_label.grid(row=0, column=4, padx=5)

root = Tk()

app = PDFViewer(root)

root.mainloop()



