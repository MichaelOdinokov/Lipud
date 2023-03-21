from tkinter import *
from math import*

from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")

#Harjutus. Lipud

#Germany
tahvel.create_rectangle(960,5, 180,45, fill="black")
tahvel.create_rectangle(960,45, 180,99, fill="red")
tahvel.create_rectangle(960,135, 180,99, fill="yellow")

#Eesti
tahvel.create_rectangle(360,5, 180,45, fill="blue")
tahvel.create_rectangle(360,45, 180,99, fill="black")
tahvel.create_rectangle(360,135, 180,99, fill="white")

#Bahama
tahvel.create_rectangle(5,5,  180,45,fill="#4599a1")
tahvel.create_rectangle(5,45,  180,90,fill="yellow")
tahvel.create_rectangle(5,130,  180,90,fill="#4599a1")
tahvel.create_polygon(5,5,  100,60,  5,130,  5,4, width=5,fill="black")

#Valgusfor
tahvel.create_line(100, 410, 135, 375, width=45, fill="red")
tahvel.create_line(100, 415, 135, 450, width=4, fill="yellow")
tahvel.create_line(100, 455, 135, 490, width=4, fill="green")
tahvel.create_rectangle(110, 490, 130, 660, fill="black", outline="black")
tahvel.create_rectangle(40, 580, 200, 620, fill="black", outline="black")



#Harjutus. Muster

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

tahvel.grid()
raam.mainloop()