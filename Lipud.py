from tkinter import *
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
tahvel.create_rectangle(100,410,  135,375,fill="red")
tahvel.create_rectangle(100,415,  135,450,fill="yellow")
tahvel.create_rectangle(100,455,  135,490,fill="green")
tahvel.create_line(30, 600, 300, 600, width=4, fill="black")
tahvel.create_line(3, 500, 30, 500, width=4, fill="black")

#Harjutus. Muster
k=7
x0=0
y0=0
x1=550
y1=550

for i in range(k):
    x0+=35
    y0+=35
    x1-=35
    y1-=35
    tahvel.create_rectangle(x0,y0,x1,y1,width=1, outline="blue", fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="yellow")



x0=10
y0=10
x1=10
y1=10
tahvel.create_rectangle(x0,y0,x1,y1,width=1, outline="black", fill="white")

tahvel.grid()
raam.mainloop()