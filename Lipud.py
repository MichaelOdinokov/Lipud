from ctypes.wintypes import FLOAT
from tkinter import *
from math import*
from tkinter import font # vajalik teksti fondi muutmiseks

aken = Tk()
aken.title("Tahvel")
tahvel = Canvas(aken, width=600, height=600, background="white")

   

def Germany():
    tahvel.create_rectangle(660,5, 180,45, fill="black")
    tahvel.create_rectangle(660,45, 180,99, fill="red")
    tahvel.create_rectangle(660,135, 180,99, fill="yellow")

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
    tahvel.create_rectangle(100, 375, 145, 420, width=1, outline="black", fill="red")
    tahvel.create_rectangle(100, 450, 145, 495, width=1, outline="black", fill="green")
    tahvel.create_rectangle(100, 525, 145, 570, width=1, outline="black", fill="yellow")
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


 # StringVar()
r1=Radiobutton(aken, text="Valgusfor",variable=IntVar, value=1,command=valgusfor) 
r2=Radiobutton(aken, text="Muster1",variable=IntVar, value=2,command=muster1) 
r3=Radiobutton(aken, text="Eesti",variable=IntVar, value=3,command=Eesti) 
r4=Radiobutton(aken, text="Germany",variable=IntVar, value=4,command=Germany) 
r5=Radiobutton(aken, text="Bahama",variable=IntVar, value=5,command=Bahama) 


r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
r4.grid(row=4,column=0)
r5.grid(row=5,column=0)

tahvel.grid()
aken.mainloop()