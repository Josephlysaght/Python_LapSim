from tkinter import *
#from CarSetup import *
from TyreSetup import *
from tkinter import filedialog

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Your shit!!!!!")
   button.pack()

def trackload():
    root.fname = filedialog.askopenfilename(title = "Select file", filetypes=(("Json Files", "*.json"),))
   
root = Tk()
root.title("Seppie LapSim")

#recieving fullscreen size
full_width = root.winfo_screenwidth()
full_height = root.winfo_screenheight()
# Setting full screen geometry 
root.geometry("%dx%d+-10+0" % (full_width, full_height))

#Creating menu
menubar = Menu(root)

#----------------------------File menu-------------------------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Set Car Parameters", command=donothing)
filemenu.add_command(label="Open Tyre Parameters", command=SetTyre)
filemenu.add_command(label="Load RaceTrack", command=trackload)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

#--------------------Edit Menu--------------------------------
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Print Report", command=donothing)
editmenu.add_command(label="Export parameters", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

#------Help Menu--------------------
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help (F1)", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#---------------------------------------------------------Main Window Display-----------------------------------------------------------------------



#------------------------------------------------------Create main view --------------------------------------------------------------------------
root.mainloop()
