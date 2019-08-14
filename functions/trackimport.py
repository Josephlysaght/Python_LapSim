#Track import tool
import json
from tkinter import *
from tkinter import filedialog
import varibles
import numpy as np

def trackload():
    if varibles.trackloaded_correctly == 1:
        master3 = Tk()
        master3.title("Confirm Track import")
        titl = Label(master3, text="Track Is already loaded!!")
        titl.pack()
        quitButton(master3)
    else:
        #prompt the user for a file to import
        filename = filedialog.askopenfilename(title = "Select file", filetypes=(("Json_full Files", "*.json_full"),))

        #Read JSON data into the datastore variable
        if filename:
          with open(filename, 'r') as f:
               varibles.trackdata = json.load(f)

        varibles.trackpoints = len (varibles.trackdata["Racing"])
        varibles.tracklenght = varibles.trackpoints * 0.5;
        n = 0
        varibles.racing_linex = np.arange(varibles.trackpoints,dtype=float)
        varibles.racing_liney = np.arange(varibles.trackpoints,dtype=float)
    
        while n < len (varibles.trackdata["Racing"]):
            varibles.racing_linex[n] = varibles.trackdata["Racing"][n][0]
            varibles.racing_liney[n] = varibles.trackdata["Racing"][n][1]
            n = n+1

        #Outputing info from import
        master = Tk()
        master.title("Confirm Track import")
        titl = Label(master, text="You have imported a map with the below details")
        titl.pack()
        name = Label(master, text="Name: " + varibles.trackdata["Name"])
        name.pack()
        quitButton(master)
        trackload.has_been_loaded = True


class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'OK - close window'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)

    

