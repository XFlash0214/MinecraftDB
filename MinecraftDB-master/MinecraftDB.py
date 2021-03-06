from firebase import firebase as fb
from tkinter import *
import json
from random import randint
import os
import imageManager as im
from tkinter import filedialog


class Pirate:
    name=""
    ship=""
    real=False
    img=""

    def getDict(self):
        d={"name":self.name,
           "color":self.ship,
           "hostile": self.real,
           "image": self.img
           }
        return d
    def lfd(self,d):
        self.name=d["name"]
        self.ship=d["color"]
        self.real=d["hostile"]
        self.img=d["image"]
class FirebaseManager:
    app=fb.FirebaseApplication("https://piratedb-0214.firebaseio.com/")
    def wrotetofile(self, idnum, obj):
        result=self.app.put("",idnum,obj)

def addNew():
    global win,namebox,shipbox,optionString,ibimg    
    p=Pirate()
    p.name=namebox.get()
    p.ship=shipbox.get()
    p.real=optionString.get()
    p.img=ibimg.cget("text")

    namebox.delete(0,"end")
    shipbox.delete(0,"end")
    optionString.set("")
    ibimg.config(text="")

    d=p.getDict()
    fm=FirebaseManager()
    idNum=randint(11111,99999)
    fm.wrotetofile(idNum,d)

    imgm=im.ImageManager()
    imgm.imagepath=win.filename
    imgm.uploadImage()
    p.img=imgm.url

    win.destroy()


def camc():
    global win
    win.destroy()

def browseImg():
    global win,ibimg
    win.filename=filedialog.askopenfilename()
    justfile=os.path.basename(win.filename)
    ibimg.config(text=justfile)

def loadwindow(root):
    global win,namebox,shipbox,optionString
    win=root
    root.title("Mob Addert")
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


    imgsel=Button(root,font="Arial 20 bold",text="Select Image",command=browseImg)
    imgsel.grid(row=4,column=0)

    ibimg=Label(root)
    ibimg.grid(row=4,column=1)

    save=Button(root,text="SAVE",font="Arial 20 bold",bg="red",command=addNew)
    save.grid(row=5,column=0,columnspan=3)

    def cancelcom():
        root.destroy()
    
    cancelbut=Button(root,text="CANCEL",command=cancelcom,font="Arial 20 bold")
    cancelbut.grid(row=6,column=0,columnspan=3)
    
    root.mainloop()
