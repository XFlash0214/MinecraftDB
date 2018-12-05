from tkinter import *
import firebase_manager
import PirateDB

window1=Tk()
window1.title("Minecraft Database")
window1.config(bg="brown")

window2=""

frame1=Frame(window1)
frame1.grid(row=0,column=0)

label1=Label(frame1,text="Minecraft Database", font="Arial 20 bold",bg="brown",fg="green")
label1.pack()

frame2=Frame(window1,padx=40,bg="brown")
frame2.grid(row=0,column=1)

entry1=Entry(frame2,font="Arial 20",bg="green")
def supdate(e):
    sfilter()

entry1.bind("<KeyRelease>", supdate)
entry1.grid(row=0,column=0)

def sfilter():
    filt=entry1.get()
    listbox.delete(0,"end")
    for pirate in d:
        if (filt.lower() in d[pirate]["name"].lower() or
        filt.lower() in d[pirate]["ship"].lower()):
            listbox.insert(END,d[pirate]["name"])

frame3=Frame(window1,bg="brown")
frame3.grid(row=1,column=0)

def display(pirateId):
    label3.config(text=d[pirateId]["name"],fg="green")
    shiplab.config(text=d[pirateId]["ship"],fg="green")
    if d[pirateId]["real"]=="True":
        reallab.config(text="Real",fg="green")
    else:
        reallab.config(text="Fake",fg="green")

def scrollr():
    index=int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index==len(d)-1:
        index=0
    else:
        index+=1
        
    ulistbox(index)

def scrolll():
    index=int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index==0:
        index=len(d)-1
    else:
        index-=1
        
    ulistbox(index)

def ulistbox(index):
    listbox.selection_set(index)
    piratename=listbox.get(index)
    for pirate in d:
        if piratename.lower()==d[pirate]["name"].lower():
            display(pirate)

label3=Label(frame3,font="Arial 30 bold",fg="black",bg="brown")
label3.grid(row=0,column=0,columnspan=3)

picImg=PhotoImage(file="profile_pic.gif")
picImg=picImg.subsample(2)
leftImg=PhotoImage(file="lefta.gif")
leftImg=leftImg.subsample(4)
rightImg=PhotoImage(file="righta.gif")
rightImg=rightImg.subsample(4)

leftb=Button(frame3,image=leftImg,command=scrolll)
leftb.grid(row=1,column=0)
rightb=Button(frame3,image=rightImg,command=scrollr)
rightb.grid(row=1,column=2)
pic=Label(frame3,image=picImg)
pic.grid(row=1,column=1)

shiplab=Label(frame3,bg="brown",font="Arial 30 bold")
shiplab.grid(row=2,column=0,columnspan=3)
reallab=Label(frame3,bg="brown",font="Arial 30 bold")
reallab.grid(row=3,column=0,columnspan=3)

frame4=Frame(window1)
frame4.grid(row=1,column=1)
frame4.config(bg="brown")

def select(e):
    w=e.widget
    index=int(w.curselection()[0])
    piratename=w.get(index)
    for pirate in d:
        if piratename.lower()==d[pirate]["name"].lower():
            display(pirate)

listbox=Listbox(frame4,font="Times 25",bg="brown",fg="green")
listbox.bind("<<ListboxSelect>>",select)
listbox.pack()
fm=firebase_manager.FirebaseManager()
d=fm.getallpirates()
for item in d:
    pirate=d[item]
    listbox.insert(END,pirate["name"])

def Listdel():
    index=int(listbox.curselection()[0])
    listbox.selection_set(index)
    piratename=listbox.get(index)
    for pirate in d:
        if piratename.lower()==d[pirate]["name"].lower():
            deletekey=pirate
    fm.deletepirate(deletekey)
    d.pop(deletekey)
    listbox.delete(ANCHOR)
    sfilter()

def npirate():
    global window2
    window2=Toplevel()
    PirateDB.loadwindow(window2)
    
delbut=Button(frame4,text="DELETE",font="Arial 20 bold",command=Listdel,bg="green",fg="brown")
delbut.pack()

newbut=Button(frame4,text="NEW MOB",font="Arial 20 bold",command=npirate,bg="green",fg="brown")
newbut.pack()

def exit0():
    window1.destroy()
extbut=Button(frame4,text="QUIT",font="Arial 20 bold",command=exit0,bg="green",fg="brown")
extbut.pack()


window1.mainloop()





