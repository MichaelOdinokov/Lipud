from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")

#Eesti
# ristkülik üksik kriips (x0, y0, x1, y1),  2-height,  1- widht, 3-
tahvel.create_rectangle(30,360,  300,300, fill="black")
tahvel.create_rectangle(30,330,  300,300, fill="blue")
tahvel.create_rectangle(30,300,  300,300, fill="white")
# võimalik on muuta joone paksust (width) ja sisu värvi (fill)
tahvel.create_line(90, 300, 90, 300, width=2, fill="black")

#Bahama
tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#42cef5") #flag
tahvel.create_rectangle(60,190, 300,170, fill="yellow")

tahvel.grid()
raam.mainloop()