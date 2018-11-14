from tkinter import *

window1=Tk()
window1.title("Pirate Database")
window1.config(bg="salmon")

frame1=Frame(window1)
frame1.grid(row=0,column=0)

label1=Label(frame1,text="Pirate Database", font="Arial 20 bold",bg="salmon")
label1.pack()

frame2=Frame(window1)
frame2.grid(row=0,column=1)

entry1=Entry(frame2,font="Arial 20")
entry1.grid(row=0,column=0)

gobut=Button(frame2,bg="green",text="Search",font="Arial 15")
gobut.grid(row=0,column=1)

frame3=Frame(window1)
frame3.grid(row=1,column=0)

label3=Label(frame3,text="Frame 3", font="Arial 20",fg="green",bg="yellow")
label3.pack()


frame4=Frame(window1)
frame4.grid(row=1,column=1)
frame4.config(bg="salmon")

listbox=Listbox(frame4,font="Airal 25",bg="light blue")
listbox.pack()
listdic={"Jerry":"1","Geri":"3","Jeri": "2","Jery":"4"}
for item in listdic:
    listbox.insert(END,item)

def Listdel():
    listbox.delete(ANCHOR)
delbut=Button(frame4,text="DELETE",font="Arial 20 bold",command=Listdel,bg="red")
delbut.pack()
def exit0():
    window1.destroy()
extbut=Button(frame4,text="QUIT",font="Arial 20 bold",command=exit0,bg="olive")
extbut.pack()


window1.mainloop()





