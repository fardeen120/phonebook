from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("database.db")
cur=con.cursor()

date=datetime.datetime.now().date()
date=str(date)


class Addpeople(Toplevel):
    def __init__(self):
     Toplevel.__init__(self)

     self.geometry("700x650+350+200")
     self.title("Add people")
     self.resizable(False,False)

     self.top = Frame(self,height="150", bg="white")
     self.top.pack(fill=X)

     self.bottom = Frame(self, height="500", bg="#639bd3")
     self.bottom.pack(fill=X)

     self.heading = Label(self.top, text="Add people", font="algerian 15 bold", bg="#0000ff", fg="light blue")
     self.heading.place(x=200, y=10)

     self.imglabel = PhotoImage(file='icons/add-group.png')
     self.imglabel.lb = Label(self.top, image=self.imglabel)
     self.imglabel.lb.place(x=120, y=10)

     self.datelabel = Label(self.top, text="today's date-" + date, font="arial 12 bold", fg="black", bg="yellow")
     self.datelabel.place(x=450, y=90)

     self.name=Label(self.bottom,text="   Name   ",font="ariel 12 bold")
     self.name.place(x=50,y=30)

     self.sirname = Label(self.bottom, text="Surname", font="ariel 12 bold")
     self.sirname.place(x=50, y=70)

     self.mobile = Label(self.bottom, text="Mobile no", font="ariel 12 bold")
     self.mobile.place(x=50, y=110)

     self.email = Label(self.bottom, text="    Email    ", font="ariel 12 bold")
     self.email.place(x=50, y=150)

     self.address = Label(self.bottom, text=" Address ", font="ariel 12 bold")
     self.address.place(x=50, y=190)

     self.entrname=Entry(self.bottom,width=40,bd=4)
     self.entrname.insert(0,"Enter name")
     self.entrname.place(x=150,y=30)

     self.entrsrname = Entry(self.bottom, width=40, bd=4)
     self.entrsrname.insert(0, "Enter surname")
     self.entrsrname.place(x=150, y=70)

     self.entrmobile = Entry(self.bottom, width=40, bd=4)
     self.entrmobile.insert(0, "Enter mobile no")
     self.entrmobile.place(x=150, y=110)

     self.entrmail = Entry(self.bottom, width=40, bd=4)
     self.entrmail.insert(0, "Enter email")
     self.entrmail.place(x=150, y=150)

     self.addtxt=Text(self.bottom,width=30,height=12)
     self.addtxt.place(x=150,y=190)

     self.exit=Button(self.bottom,text="Exit",width=4,command=self.destroy)
     self.exit.place(x=200,y=400)

     self.back = Button(self.bottom, text="Back", width=4,command=self.destroy)
     self.back.place(x=250, y=400)

     self.savebtn = Button(self.bottom, text="Add people", width=9,command=self.add_people)
     self.savebtn.place(x=300, y=400)

    def add_people(self):
     name=self.entrname.get()
     sirname=self.entrsrname.get()
     mobile=self.entrmobile.get()
     email=self.entrmail.get()
     address=self.addtxt.get(1.0,'end-1c')

     if name and sirname and mobile and email and address!= "":
      try:
       query="insert into 'phonebook' (f_name, l_name, mobile_no, mail_add, per_address) values(?,?,?,?,?)"
       cur.execute(query,(name,sirname,mobile,email,address))
       con.commit()
       messagebox.showinfo("success", "contacts added")
      except EXCEPTION as e:
       messagebox.showerror("error",str(e))
     else:
      messagebox.showerror("error","fill all details",icon="warning")

