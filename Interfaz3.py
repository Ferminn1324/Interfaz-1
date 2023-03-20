from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry("1000x1000")
raiz.configure(background="black")

MenuFrame = ttk.Frame(raiz,background="turquoise4")
MenuFrame.grid(column=0,row=0, sticky=(W))

FrameP = ttk.Frame(raiz, background="black")
FrameP.grid(column=0, row=1, sticky=(W), pady=10)

#frames izquierda arriba

frameIzquierda = ttk.Frame(FrameP,background="black")
frameIzquierda.grid(column=0,row=0,pady=10,sticky=(W,N))

Frame1 = ttk.Frame(frameIzquierda,background="black")
Frame1.grid(column=0,row=0,sticky=(W))

IzqFrame = ttk.Frame(Frame1,background="#333333")
IzqFrame.grid(column=0,row=0,sticky=(W),padx=5)

DerFrame = ttk.Frame(Frame1,background="#333333")
DerFrame.grid(column=1,row=0,sticky=(W,N))

#framederecha

framederecha = ttk.Frame(FrameP,background="#333333")
framederecha.grid(column=1,row=0,sticky=(W,N),padx=5)

frame3 = ttk.Frame(framederecha,background="#333333")
frame3.grid(column=0,row=0, sticky=(W,N))

produccionFrame = ttk.Frame(frame3,background="#333333")
produccionFrame.grid(column=2,row=0,sticky=(W,N))

#frame izquierda 

Frame2 = ttk.Frame(frameIzquierda,background="black")
Frame2.grid(column=0,row=1,sticky=(W,N))

DerAbajoFrame = ttk.Frame(Frame2,background="#333333")
DerAbajoFrame.grid(column=0,row=0,sticky=(W,N),padx=5,pady=5)

DerAbajoFrame1 = ttk.Frame(Frame2,background="#333333")
DerAbajoFrame1.grid(column=1,row=0,sticky=(W),padx=5)

ttk.Label(MenuFrame,text="SPAI 4.0",font=("verdana",18,"bold"),foreground="white",background="turquoise4", width=200,anchor="w",height=2).grid(column=1,row=0,sticky=(W))

ttk.Label(IzqFrame,text="Indicadores Digitales",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333", width=20).grid(column=0,row=0,sticky=(W))
ttk.Label(IzqFrame,text="Linea 1:       On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=1,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Linea 2:       On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=2,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Linea 1:       On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=3,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Gabinete: Abierto",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=4,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Alarma:        On",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=5,sticky=(W),pady=11)
ttk.Label(IzqFrame,text="Alarma 2:     Off",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=6,sticky=(W),pady=11)

ttk.Label(DerFrame,text="Temperatura",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W))
ttk.Label(DerFrame,text="Temperatura 1:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=1,sticky=(W),pady=30,padx=15)
ttk.Label(DerFrame,text="Temperatura 2:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=1,row=1,sticky=(W),pady=30)
ttk.Label(DerFrame,text="Temp.Agua: 58 °C",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=3,sticky=(N,S),columnspan=2)
ttk.Label(DerFrame,text="Temp.Ambiente: 32 °C",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=4,sticky=(N,S),columnspan=2,pady=10)

ttk.Label(produccionFrame,text="Produccion",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W),padx=30)

ttk.Label(DerAbajoFrame,text="Velocidad Bomba:",font=("verdana",13,"bold"),foreground="white",background="#333333").grid(column=0,row=0,sticky=(W))

ttk.Label(DerAbajoFrame1,text="Nivel del Tanque",font=("verdana",13,"bold"),foreground="turquoise4",background="#333333").grid(column=0,row=0,sticky=(W))

imagen3 = PhotoImage(file="boton.png")
imagenb = ttk.Button(MenuFrame,background="turquoise4",relief="flat")
imagenb.grid(column=0,row=0,sticky=(W))
imagenb['image'] = imagen3

imagen5 = PhotoImage(file="tem1.png")
imagenT1 = ttk.Button(DerFrame,background="#333333",relief="flat")
imagenT1.grid(column=0,row=2,sticky=(W))
imagenT1['image'] = imagen5

imagen6 = PhotoImage(file="tem2.png")
imagenT2 = ttk.Button(DerFrame,background="#333333",relief="flat")
imagenT2.grid(column=1,row=2,sticky=(W))
imagenT2['image'] = imagen6

imagen7 = PhotoImage(file="imagenG.png")
imagenG = ttk.Button(produccionFrame,background="#333333",relief="flat")
imagenG.grid(column=0,row=1,sticky=(W))
imagenG['image'] = imagen7

imagen8 = PhotoImage(file="imagen 4.png")
imagen4 = ttk.Button(DerAbajoFrame,background="#333333",relief="flat")
imagen4.grid(column=0,row=1,sticky=(W))
imagen4['image'] = imagen8

imagen9 = PhotoImage(file="imagen tanque.png")
imagenTan = ttk.Button(DerAbajoFrame1,background="#333333",relief="flat")
imagenTan.grid(column=0,row=1,sticky=(W))
imagenTan['image'] = imagen9








raiz.mainloop()