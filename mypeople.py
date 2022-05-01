from tkinter import *
import sqlite3
import datetime
from addpeople import Addpeople
from update import Updateppl


date=datetime.datetime.now().date()
date=str(date)

con=sqlite3.connect("database.db")
cur=con.cursor()

class Mypeople(Toplevel):
    def __init__(self):
     Toplevel.__init__(self)

     self.geometry("700x650+350+200")
     self.title("My people")
     self.resizable(False, False)

     self.top = Frame(self, height="150", bg="white")
     self.top.pack(fill=X)

     self.bottom = Frame(self, height="500", bg="#639bd3")
     self.bottom.pack(fill=X)

     self.heading = Label(self.top, text="My people", font="algerian 15 bold", bg="#0000ff", fg="light blue")
     self.heading.place(x=200, y=10)

     self.imglabel = PhotoImage(file='icons/my people.png')
     self.imglabel.lb = Label(self.top, image=self.imglabel)
     self.imglabel.lb.place(x=120, y=10)

     self.datelabel = Label(self.top, text="today's date-" + date, font="arial 12 bold", fg="black", bg="yellow")
     self.datelabel.place(x=450, y=90)

     self.scroll=Scrollbar(self.bottom, orient=VERTICAL)

     self.listbox=Listbox(self.bottom, width=40, height=31)
     self.listbox.grid(row=0, column=0, padx=(40,0))
     self.scroll.config(command=self.listbox.yview)
     self.listbox.config(yscrollcommand=self.scroll.set)
     persons=cur.execute("select * from 'phonebook'").fetchall()
     count=0

     for person in persons:
      self.listbox.insert(count, str(person[0])+  "."  +person[1]+" "+person[2])
      count +=1



     self.scroll.grid(row=0, column=1, sticky=N+S)

     btnadd=Button(self.bottom,text="Add",width=12,font="sans 12 bold",command=self.ad_ppl)
     btnadd.grid(row=0,column=3,padx=20,pady=10,sticky=N)

     btnupd = Button(self.bottom, text="Update", width=12, font="sans 12 bold",command=self.update_function)
     btnupd.grid(row=0, column=3, padx=30, pady=60, sticky=N)

     btndsp = Button(self.bottom, text="Display", width=12, font="sans 12 bold")
     btndsp.grid(row=0, column=3, padx=40, pady=110, sticky=N)

     btndlt = Button(self.bottom, text="Delete", width=12, font="sans 12 bold")
     btndlt.grid(row=0, column=3, padx=50, pady=160, sticky=N)

     btbck = Button(self.bottom, text="back", width=12, font="sans 12 bold",command=self.destroy)
     btbck.grid(row=0, column=3, padx=60, pady=210, sticky=N)

    def ad_ppl(self):

     newpage=Addpeople()
     self.destroy()

    def update_function(self):

     selected_items=self.listbox.curselection()

     person=self.listbox.get(selected_items)

     person_id=person.split(".")[0]
     print(person_id)

     update=Updateppl(person_id)
     self.destroy()













