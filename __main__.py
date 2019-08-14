import tkinter
from functions.CarSetup import *
from functions.TyreSetup import *
from functions.curvaturecalc import *
from functions.trackimport import *
import varibles
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Your shit!!!!!")
   button.pack()
   
root = Tk()
root.title("Seppie LapSim")

#recieving fullscreen size
full_width = root.winfo_screenwidth()
full_height = root.winfo_screenheight()
# Setting full screen geometry 
#root.geometry("%dx%d+-10+0" % (full_width, full_height))
root.geometry("%dx%d+-10+0" % (200, 200))
#Creating menu
menubar = Menu(root)

#----------------------------File menu-------------------------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Set Car Parameters", command=carsettings)
filemenu.add_command(label="Open Tyre Parameters", command=SetTyre)
filemenu.add_command(label="Load RaceTrack", command=trackload)
filemenu.add_command(label="Something Else", command=donothing)
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
trackload.has_been_loaded = False
carsettings.has_been_loaded = False
n = 0
while True:
    root.update_idletasks()
    root.update()

         #-------------------------------Plot track when loaded ------------------------------------------------    
    if trackload.has_been_loaded:

       calccur()
       apexfinder()
       
       fig = Figure(figsize=(5, 4), dpi=100)
       fig.add_subplot(111).plot(varibles.racing_linex,varibles.racing_liney)

       canvas = FigureCanvasTkAgg(fig, master=root)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
       trackload.has_been_loaded = False
       
