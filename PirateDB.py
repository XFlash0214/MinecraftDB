from tkinter import *
import json
from random import randint
class Pirate:
    name=""
    ship=""
    real=False

    def getDict(self):
        d={"name":self.name,
           "ship":self.ship,
           "real": self.real
           }
        return d
    def lfd(self,d):
        self.name=d["name"]
        self.ship=d["ship"]
        self.real=d["real"]
class FileManager:
    path="PirateDB.json"
    def wrotetofile(self, idnum, obj):
        try:
            f=open(self.path,"r")
            d=json.load(f)
            f.close()
        except:
            d={}
        d[idnum]=obj
        f=open(self.path,"w")
        json.dump(d,f)
        f.close()

def addNew():
    p=Pirate()
    p.name=namebox.get()
    p.ship=shipbox.get()
    p.real=optionString.get()

    namebox.delete(0,"end")
    shipbox.delete(0,"end")

    d=p.getDict()
    fm=FileManager()
    idNum=randint(11111,99999)
    fm.wrotetofile(idNum,d)
    
root=Tk()
root.title("Pirate Database")
root.config(bg="blue")

title=Label(root,text="Pirate Database", font="Arial 30 bold",bg="blue")
title.grid(row=0,column=0,columnspan=3)

nametk=Label(root,text="Name:", font="Arial 20",bg="blue")
nametk.grid(row=1,column=0,columnspan=1)

namebox=Entry(root, font="Arial 20",bg="blue")
namebox.grid(row=1,column=2)

shiptk=Label(root,text="Ship:", font="Arial 20",bg="blue")
shiptk.grid(row=2,column=0,columnspan=1)

shipbox=Entry(root, font="Arial 20",bg="blue")
shipbox.grid(row=2,column=2)

realtk=Label(root,text="Real:", font="Arial 20",bg="blue")
realtk.grid(row=3,column=0,columnspan=1)

optionString=StringVar(root)
optionString.set(" ")
dropdown=OptionMenu(root,optionString," ","True","False")
dropdown.config(font="Arial 20",width="17",bg="blue")
dropdown.nametowidget(dropdown.menuname).config(font="Arial 20")
dropdown.grid(row=3,column=2)


save=Button(root,text="SAVE",font="Arial 20 bold",bg="red",command=addNew)
save.grid(row=4,column=1,columnspan=2)

root.mainloop()
