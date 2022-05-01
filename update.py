from tkinter import *
import sqlite3
import datetime
from addpeople import Addpeople

date=datetime.datetime.now().date()
date=str(date)

con=sqlite3.connect("database.db")
cur=con.cursor()

class Updateppl(Toplevel):
    def __init__(self,person_id):
     Toplevel.__init__(self)

     query="select * from phonebook where id ='{}'".format(person_id)
     result=cur.execute(query).fetchone()
     name=result[1]
     sirname=result[2]
     mobile=result[3]
     email=result[4]
     address=result[5]
     print(name,sirname,mobile,email,address)

     self.geometry("700x650+350+200")
     self.title("Update people")
     self.resizable(False, False)

     self.top = Frame(self, height="150", bg="white")
     self.top.pack(fill=X)

     self.bottom = Frame(self, height="500", bg="#639bd3")
     self.bottom.pack(fill=X)

     self.heading = Label(self.top, text="Update people", font="algerian 15 bold", bg="#0000ff", fg="light blue")
     self.heading.place(x=200, y=10)

     self.imglabel = PhotoImage(file='icons/my people.png')
     self.imglabel.lb = Label(self.top, image=self.imglabel)
     self.imglabel.lb.place(x=120, y=10)

     self.datelabel = Label(self.top, text="today's date-" + date, font="arial 12 bold", fg="black", bg="yellow")
     self.datelabel.place(x=450, y=90)

     self.name = Label(self.bottom, text="   Name   ", font="ariel 12 bold")
     self.name.place(x=50, y=30)

     self.sirname = Label(self.bottom, text="Surname", font="ariel 12 bold")
     self.sirname.place(x=50, y=70)

     self.mobile = Label(self.bottom, text="Mobile no", font="ariel 12 bold")
     self.mobile.place(x=50, y=110)

     self.email = Label(self.bottom, text="    Email    ", font="ariel 12 bold")
     self.email.place(x=50, y=150)

     self.address = Label(self.bottom, text=" Address ", font="ariel 12 bold")
     self.address.place(x=50, y=190)

     self.entrname = Entry(self.bottom, width=40, bd=4)
     self.entrname.insert(0, name)
     self.entrname.place(x=150, y=30)

     self.entrsrname = Entry(self.bottom, width=40, bd=4)
     self.entrsrname.insert(0, sirname)
     self.entrsrname.place(x=150, y=70)

     self.entrmobile = Entry(self.bottom, width=40, bd=4)
     self.entrmobile.insert(0, mobile)
     self.entrmobile.place(x=150, y=110)

     self.entrmail = Entry(self.bottom, width=40, bd=4)
     self.entrmail.insert(0, email)
     self.entrmail.place(x=150, y=150)

     self.addtxt = Text(self.bottom, width=30, height=12)
     self.addtxt.place(x=150, y=190)
     self.addtxt.insert(1.0,address)

     self.upd = Button(self.bottom, text="Update", width=5)
     self.upd.place(x=200, y=400)

     self.back = Button(self.bottom, text="Back", width=4, command=self.destroy)
     self.back.place(x=250, y=400)

     self.ext = Button(self.bottom, text="Exit", width=4,command=self.destroy)
     self.ext.place(x=290, y=400)




