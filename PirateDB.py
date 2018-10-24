from tkinter import *
import json
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
class FileManger:
    path="PirateDB.json"
    def wtf(self, idnum, obj):
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
    x=0

root=Tk()
root.title("Pirate Database")
root.config(bg="pink")

title=Label(root,text="Pirate Database", font="Arial 30 bold",bg="pink")
title.grid(row=0,column=0,columnspan=3)

nametk=Label(root,text="Name:", font="Arial 20",bg="pink")
nametk.grid(row=1,column=0,columnspan=1)

namebox=Entry(root, font="Arial 20")
namebox.grid(row=1,column=2)

shiptk=Label(root,text="Ship:", font="Arial 20",bg="pink")
shiptk.grid(row=2,column=0,columnspan=1)

shipbox=Entry(root, font="Arial 20")
shipbox.grid(row=2,column=2)

realtk=Label(root,text="Real:", font="Arial 20",bg="pink")
realtk.grid(row=3,column=0,columnspan=1)

optionString=StringVar(root)
optionString.set(" ")
dropdown=OptionMenu(root,optionString," ","True","False")
dropdown.config(font="Arial 20",width="17")
dropdown.nametowidget(dropdown.menuname).config(font="Arial 20")
dropdown.grid(row=3,column=2)


save=Button(root,text="SAVE",font="Arial 20 bold",bg="red",command=addNew)
save.grid(row=4,column=1,columnspan=2)

root.mainloop()
