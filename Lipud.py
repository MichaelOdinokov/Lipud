from ctypes.wintypes import FLOAT
from tkinter import *
from math import*
from tkinter import font # vajalik teksti fondi muutmiseks

aken = Tk()
aken.title("Tahvel")
tahvel = Canvas(aken, width=600, height=600, background="white")

def valik():# Vigade expected floating-point number but got "2383169571200muster1"
    val1=var.get()
    val2=var.get()  
    if val1!="-": val1.insert(END, val1)
    if val2!="--":val2.insert(END, val2)
   

def Germany():
    tahvel.create_rectangle(960,5, 180,45, fill="black")
    tahvel.create_rectangle(960,45, 180,99, fill="red")
    tahvel.create_rectangle(960,135, 180,99, fill="yellow")

def Eesti():
    tahvel.create_rectangle(360,5, 180,45, fill="blue")
    tahvel.create_rectangle(360,45, 180,99, fill="black")
    tahvel.create_rectangle(360,135, 180,99, fill="white")

def Bahama():
    tahvel.create_rectangle(5,5,  180,45,fill="#4599a1")
    tahvel.create_rectangle(5,45,  180,90,fill="yellow")
    tahvel.create_rectangle(5,130,  180,90,fill="#4599a1")
    tahvel.create_polygon(5,5,  100,60,  5,130,  5,4, width=5,fill="black")

def valgusfor():
    tahvel.create_line(100, 410, 135, 375, width=45, fill="red")
    tahvel.create_line(100, 415, 135, 450, width=45, fill="yellow")
    tahvel.create_line(100, 455, 135, 490, width=45, fill="green")
    tahvel.create_rectangle(110, 490, 130, 660, fill="black")
    tahvel.create_rectangle(40, 580, 200, 620, fill="black")

def muster1():
    x0=400
    y0=400
    x1=600
    y1=600
    a=100
    r=(a**2+a**2)**(1/2)
    p=(a-r)

    for i in range(12):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        tahvel.create_rectangle(x0,y0,x1,y1,width=1, outline="blue", fill="red")
        tahvel.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2


var=IntVar() # StringVar()
r1=Radiobutton(aken, text="Valgusfor",variable=var, value=valgusfor,command=valik) # variable=var svjazali, znachenija var=1
r2=Radiobutton(aken, text="Muster1",variable=var, value=muster1,command=valik) # variable=var svjazali, znachenija var=2
r3=Radiobutton(aken, text="Eesti",variable=var, value=Eesti,command=valik) # variable=var svjazali, znachenija var=2
r4=Radiobutton(aken, text="Germany",variable=var, value=Germany,command=valik) # variable=var svjazali, znachenija var=2
r5=Radiobutton(aken, text="Bahama",variable=var, value=Bahama,command=valik) # variable=var svjazali, znachenija var=2


r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
r4.grid(row=4,column=0)
r5.grid(row=5,column=0)





tahvel.grid()
aken.mainloop()