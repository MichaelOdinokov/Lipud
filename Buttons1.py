from email.mime import image
from tkinter import*



def valik():
    num=var.get()# var.get()-read var
    lbox.insert(END, num)# v konze kazhdi raz pojavljaetsja novoe znachenija

def valik_2():
    val1=var.get()
    val2=var.get()
    val3=var.get()   
    if val1!="-": lbox.insert(END, val1)
    if val2!="--":lbox.insert(END, val2)
    if val3!="---":lbox.insert(END, val3)

aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")
    


var=IntVar() # StringVar()
r1=Radiobutton(aken, text="Esimene",variable=var, value=1,command=valik)# variable=var svjazali, znachenija var=1
r2=Radiobutton(aken, text="Teine",variable=var, value=2,command=valik)# variable=var svjazali, znachenija var=2
r3=Radiobutton(aken, text="Kolmas",variable=var, value=3,command=valik)# variable=var svjazali, znachenija var=2, (command=valik(a))
lbox=Listbox(aken,height=9, width=30)

var1=StringVar()
var2=StringVar()
var3=StringVar()
c1=Checkbutton(aken,text="Esimene",variable=var1,onvalue="Esimene",offvalue="-",command=valik_2)
c2=Checkbutton(aken,text="Teine",variable=var2,onvalue="Teine",offvalue="--",command=valik_2)
c3=Checkbutton(aken,text="Kolmas",variable=var3,onvalue="Kolmas",offvalue="---",command=valik_2)







lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)

c1.grid(row=1, column=1)
c2.grid(row=2, column=1)
c3.grid(row=3, column=1)
c1.deselect()
c2.deselect()
c3.deselect()

aken.mainloop()




