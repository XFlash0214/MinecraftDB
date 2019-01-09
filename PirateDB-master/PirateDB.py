from firebase import firebase as fb
from tkinter import *
import json
from random import randint

def browseimg():
    x=0
    
class Pirate:
    name=""
    ship=""
    real=False
    img=""

    def getDict(self):
        d={"name":self.name,
           "color":self.ship,
           "hostile": self.real,
           "img": self.img
           }
        return d
    def lfd(self,d):
        self.name=d["name"]
        self.ship=d["color"]
        self.real=d["hostile"]
class FirebaseManager:
    app=fb.FirebaseApplication("https://piratedb-0214.firebaseio.com/")
    def wrotetofile(self, idnum, obj):
        result=self.app.put("",idnum,obj)

def addNew():
    global win,namebox,shipbox,optionString    
    p=Pirate()
    p.name=namebox.get()
    p.ship=shipbox.get()
    p.real=optionString.get()

    namebox.delete(0,"end")
    shipbox.delete(0,"end")

    d=p.getDict()
    fm=FirebaseManager()
    idNum=randint(11111,99999)
    fm.wrotetofile(idNum,d)

    win.destroy()

def loadwindow(root):
    global win,namebox,shipbox,optionString, ibimg
    win=root
    root.title("Mob Adder")
    root.config(bg="brown")

    title=Label(root,text="Minecraft Adder", font="Arial 30 bold",bg="brown")
    title.grid(row=0,column=0,columnspan=3)

    nametk=Label(root,text="Name:", font="Arial 20",bg="brown")
    nametk.grid(row=1,column=0,columnspan=1)

    namebox=Entry(root, font="Arial 20",bg="brown")
    namebox.grid(row=1,column=2)

    shiptk=Label(root,text="Color:", font="Arial 20",bg="brown")
    shiptk.grid(row=2,column=0,columnspan=1)

    shipbox=Entry(root, font="Arial 20",bg="brown")
    shipbox.grid(row=2,column=2)

    realtk=Label(root,text="Hostile:", font="Arial 20",bg="brown")
    realtk.grid(row=3,column=0,columnspan=1)

    optionString=StringVar(root)
    optionString.set(" ")
    dropdown=OptionMenu(root,optionString," ","True","False")
    dropdown.config(font="Arial 20",width="17",bg="brown")
    dropdown.nametowidget(dropdown.menuname).config(font="Arial 20")
    dropdown.grid(row=3,column=2)


    save=Button(root,text="SAVE",font="Arial 20 bold",bg="red",command=addNew)
    save.grid(row=4,column=0,columnspan=3)

    imgbut=Button(root,text="IMAGE",font="Arial 20 bold", bg="blue",command=browseimg)
    imgbut.grid(row=7,column=1)
    
    #ibimg=Label(root,)
    
    def cancelcom():
        root.destroy()
    
    cancelbut=Button(root,text="CANCEL",command=cancelcom,font="Arial 20 bold")
    cancelbut.grid(row=5,column=0,columnspan=3)
    
    root.mainloop()
