from tkinter import *
from tkinter import filedialog
import pandas as pd

def importfile():
   import_file_path = filedialog.askopenfilename()
   df = pd.read_csv (import_file_path, sep = '\t')


#def SetCar():
#---------------------------Set up window ----------------------
root = Tk()
root.title("Import Car Parameters")
#root.geometry("400x400+200+200")

heading1 = Label(root, text="    Please import setup sheet or set manually", font=("Helvetica", 12)).grid(row=0, column=0+1)
importb = Button(root, text ="Import setup sheet", command = importfile ).grid(row=1, column=1)
Break = Label(root, text=" ").grid(row=2, column=2)

#-------------------Taking in settings ------------------------
Label(root, text="Trackwidth").grid(row=3, column=0)
Label(root, text="Wheelbase").grid(row=4, column=0)
Label(root, text="Camber").grid(row=5, column=0)
Label(root, text="Caster").grid(row=6, column=0)

trackwidth = Entry(root)
wheelbase = Entry(root)
camber = Entry(root)
caster = Entry(root)

trackwidth.grid(row=3, column=1)
wheelbase.grid(row=4, column=1)
camber.grid(row=5, column=1)
caster.grid(row=6, column=1)

root.mainloop()

def importfile():
   import_file_path = filedialog.askopenfilename()
   df = pd.read_csv (import_file_path, sep = '\t')
