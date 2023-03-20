
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
#Harjutus. Lipud
#Eesti
tahvel.create_rectangle(360,5, 180,45, fill="blue")
tahvel.create_rectangle(360,45, 180,99, fill="black")
tahvel.create_rectangle(360,135, 180,99, fill="white")

#Bahama
tahvel.create_rectangle(5,5,  180,45,fill="#4599a1")
tahvel.create_rectangle(5,45,  180,90,fill="yellow")
tahvel.create_rectangle(5,130,  180,90,fill="#4599a1")
tahvel.create_polygon(5,5,  100,60,  5,130,  5,4, width=5,fill="black")

tahvel.create_rectangle(100,410,  135,375,fill="red")
tahvel.create_rectangle(100,415,  135,450,fill="yellow")
tahvel.create_rectangle(100,455,  135,490,fill="green")



tahvel.grid()
raam.mainloop()