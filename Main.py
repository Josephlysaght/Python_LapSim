from tkinter import *
from datahandler import * #Used to handle all data import, export and handeling tasks
 
def importws():
   filewin = Toplevel(root)
   button = Button(filewin, text="Load Workspace")
   button.pack()
   
def savews():
   filewin = Toplevel(root)
   button = Button(filewin, text="Save Workspace")
   button.pack()
   
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Your shit!!!!!")
   button.pack()
   
root = Tk()

#recieving fullscreen size
full_width = root.winfo_screenwidth()
full_height = root.winfo_screenheight()

# Setting full screen geometry 
root.geometry("%dx%d+-10+0" % (full_width, full_height))
root.configure(background='black')

#Creating menu
menubar = Menu(root)

#----------------------------File menu-------------------------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Workspace", command=donothing)
filemenu.add_command(label="Open Data File", command=importfile)
filemenu.add_command(label="Save Workspace", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#--------------------Edit Menu--------------------------------
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo all zoom ", command=donothing)
editmenu.add_command(label="Export as CSV", command=donothing)
editmenu.add_command(label="Add lap trigger", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

#------Help Menu--------------------
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help (F1)", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#---------------------------------------------------------Creating layout-----------------------------------------------------------------------
left_width = full_width/4
full_height = full_height
right_width = full_width-left_width
right_height = full_height/2

# Left and right split
left = Frame ( root, bd="2", width=left_width, height=left_height, bg="red")
right = Frame ( root, bd="2", width=right_width, height = right_height,bg="green")

# Left organiser

left.place(x=0, y=0)
right.place(x=left_width, y=0)

#------------------------------------------------------Create main view --------------------------------------------------------------------------
root.mainloop()