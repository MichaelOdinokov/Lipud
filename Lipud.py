
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
#Harjutus. Lipud
#Eesti
tahvel.create_rectangle(5,5, 180,45, fill="blue")
tahvel.create_rectangle(5,45, 180,99, fill="black")
tahvel.create_rectangle(5,135, 180,99, fill="white")

#Bahama
tahvel.create_rectangle(360,5, 180,45, fill="#42cef5")
tahvel.create_rectangle(360,45, 180,99, fill="yellow")
tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="black")
tahvel.create_rectangle(360,130, 180,99, fill="#42cef5")


tahvel.grid()
raam.mainloop()