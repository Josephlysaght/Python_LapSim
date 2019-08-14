from tkinter import *
from tkinter import filedialog
import pandas as pd
import varibles

def importfile():
   import_file_path = filedialog.askopenfilename()
   df = pd.read_csv (import_file_path, sep = '\t')


def carsettings():
#---------------------------Set up window ----------------------
   carmaster = Tk()
   carmaster.title("Import Car Parameters")
   carmaster.geometry("400x400+200+200")

   heading1 = Label(carmaster, text="    Please import setup sheet or set manually", font=("Helvetica", 12)).grid(row=0, column=0+1)
   importb = Button(carmaster, text ="Import setup sheet", command = importfile ).grid(row=1, column=1)
   Break = Label(carmaster, text=" ").grid(row=2, column=2)

#-------------------Taking in settings ------------------------
   Label(carmaster, text="Trackwidth").grid(row=3, column=0)
   Label(carmaster, text="Wheelbase").grid(row=4, column=0)
   Label(carmaster, text="Camber").grid(row=5, column=0)
   Label(carmaster, text="Caster").grid(row=6, column=0)
   Label(carmaster, text="Toe").grid(row=7, column=0)

   trackwidth = Entry(carmaster)
   wheelbase = Entry(carmaster)
   camber = Entry(carmaster)
   caster = Entry(carmaster)
   toe = Entry(carmaster)

   trackwidth.grid(row=3, column=1)
   wheelbase.grid(row=4, column=1)
   camber.grid(row=5, column=1)
   caster.grid(row=6, column=1)
   toe.grid(row=7, column=1)

   quitButton(carmaster)

   while True:
      carmaster.update_idletasks()
      carmaster.update()
      varibles.trackwidth = trackwidth.get()
      varibles.wheelbase = wheelbase.get()
      varibles.camber = camber.get()
      varibles.caster = caster.get()
      varibles.toe = toe.get()

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = '   OK    '      
        self['command'] = parent.destroy
        self.grid(row=8,column=1)

   
