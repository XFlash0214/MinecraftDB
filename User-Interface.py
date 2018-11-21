from tkinter import *

window1=Tk()
window1.title("Minecraft Database")
window1.config(bg="green")

frame1=Frame(window1)
frame1.grid(row=0,column=0)

label1=Label(frame1,text="Minecraft Database", font="Arial 20 bold",bg="green")
label1.pack()

frame2=Frame(window1,padx=40,bg="green")
frame2.grid(row=0,column=1)

entry1=Entry(frame2,font="Arial 20")
entry1.grid(row=0,column=0)

gobut=Button(frame2,bg="green",text="Search",font="Arial 15")
gobut.grid(row=0,column=1)

frame3=Frame(window1,bg="green")
frame3.grid(row=1,column=0)

label3=Label(frame3,text="Place Holder", font="Arial 20",fg="green",bg="green")
label3.grid(row=0,column=0,columnspan=3)

picImg=PhotoImage(file="profile_pic.gif")
picImg=picImg.subsample(2)
leftImg=PhotoImage(file="lefta.gif")
leftImg=leftImg.subsample(4)
rightImg=PhotoImage(file="righta.gif")
rightImg=rightImg.subsample(4)

leftb=Button(frame3,image=leftImg)
leftb.grid(row=1,column=0)
rightb=Button(frame3,image=rightImg)
rightb.grid(row=1,column=2)
pic=Label(frame3,image=picImg)
pic.grid(row=1,column=1)

shiplab=Label(frame3,text="SHIP=",bg="green",font="Arial 30 bold")
shiplab.grid(row=2,column=0,columnspan=3)
reallab=Label(frame3,text="REAL=",bg="green",font="Arial 30 bold")
reallab.grid(row=3,column=0,columnspan=3)

frame4=Frame(window1)
frame4.grid(row=1,column=1)
frame4.config(bg="green")

listbox=Listbox(frame4,font="Airal 25",bg="light blue")
listbox.pack()
listdic={"Jerry":"1","Geri":"3","Jeri": "2","Jery":"4"}
for item in listdic:
    listbox.insert(END,item)

def Listdel():
    listbox.delete(ANCHOR)
delbut=Button(frame4,text="DELETE",font="Arial 20 bold",command=Listdel,bg="brown",fg="green")
delbut.pack()
def exit0():
    window1.destroy()
extbut=Button(frame4,text="QUIT",font="Arial 20 bold",command=exit0,bg="brown",fg="green")
extbut.pack()


window1.mainloop()





