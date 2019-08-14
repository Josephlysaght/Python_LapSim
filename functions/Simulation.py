import varibles
from tkinter import *

def start():
    if varibles.trackloaded_correctly == 0:
        master1 = Tk()
        master1.title("Warning!!!")
        titl = Label(master1, text="Please Load a track map first")
        titl.pack()
        quitButton(master1)
    elif varibles.carloaded_correctly == 0:
        master2 = Tk()
        master2.title("Warning!!!")
        titl = Label(master2, text="Load car parameters first!!!")
        titl.pack()
        quitButton(master2)
    elif varibles.tyreloaded_correctly == 0:
        master4 = Tk()
        master4.title("Warning!!!")
        titl = Label(master4, text="Load tyre parameters first!!!")
        titl.pack()
        quitButton(master4)
    else:
        master5 = Tk()
        master5.title("Warning!!!")
        titl = Label(master5, text="Good to go!!!")
        titl.pack()
        quitButton(master5)

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'OK'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)