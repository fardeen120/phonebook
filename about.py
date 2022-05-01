from tkinter import *

class Aboutus(Toplevel):
    def __init__(self):
     Toplevel.__init__(self)

     self.geometry("700x650+350+200")
     self.title("About us")
     self.resizable(False,False)

     self.top = Frame(self, height="650", bg="light pink")
     self.top.pack(fill=X)


