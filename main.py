from tkinter import *
import datetime
from mypeople import Mypeople
from addpeople import Addpeople
from about import Aboutus

date=datetime.datetime.now().date()
date=str(date)



class Application():
    def __init__(self,master):
     self.master=master

     self.top=Frame(master,height="150",bg="white")
     self.top.pack(fill=X)

     self.bottom=Frame(master,height="500",bg="#639bd3")
     self.bottom.pack(fill=X)

     self.heading=Label(self.top,text="My phonebook",font="algerian 15 bold",bg="#0000ff",fg="light blue")
     self.heading.place(x=170,y=10)

     self.imglabel=PhotoImage(file='icons/phone.png')
     self.imglabel.lb=Label(self.top,image=self.imglabel)
     self.imglabel.lb.place(x=120,y=10)

     self.datelabel=Label(self.top,text="today's date-"+date,font="arial 12 bold",fg="black",bg="yellow")
     self.datelabel.place(x=450,y=90)

     self.button1=Button(self.bottom,text="Add people",fg="white",bg="#8000ff",font="aeiel 12 bold",command=self.add_people)
     self.button1.place(x=300,y=70)

     self.button2 = Button(self.bottom, text=" My people ",fg="white",bg="#8000ff",font="aeiel 12 bold",command=self.my_people)
     self.button2.place(x=300, y=120)

     self.button3 = Button(self.bottom, text="  About us  ",fg="white",bg="#8000ff",font="aeiel 12 bold",command=self.about_us)
     self.button3.place(x=300, y=170)


    def my_people(self):
     people=Mypeople()

    def add_people(self):
     add=Addpeople()

    def about_us(self):
     abt=Aboutus()





root = Tk()
root.title("Phonebook")
root.geometry("700x650+350+200")
root.resizable(False,False)
app=Application(root)
root.mainloop()





