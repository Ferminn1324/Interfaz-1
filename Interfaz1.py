from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk

# Crear una ventana raíz
root = Tk()

# Crear un notebook (panel tabulado)
notebook = ttk.Notebook(root)
notebook.configure(width=600, height=450)

# Crear pestañas dentro del notebook
ADD = ttk.Frame(notebook)
ADD.configure(width=100)
Delete = ttk.Frame(notebook)
Delete.configure(width=100)
Search = ttk.Frame(notebook)
Search.configure(width=100)
Service = ttk.Frame(notebook)
Service.configure(width=100)
THelp = ttk.Frame(notebook)
THelp.configure(width=100)

# Modificar el estilo por defecto de las etiquetas
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14))

# Agregar widgets a cada pestaña
ttk.Label(ADD).grid(column=0, row=0, padx=10, pady=10)
ttk.Label(Delete).grid(column=0, row=0, padx=10, pady=10)
ttk.Label(Search).grid(column=0, row=0, padx=10, pady=10)
ttk.Label(Service).grid(column=0, row=0, padx=10, pady=10)
ttk.Label(THelp).grid(column=0, row=0, padx=10, pady=10)

# Agregar las pestañas al notebook
notebook.add(ADD, text="       Add      ")
notebook.add(Delete, text="       Delete      ")
notebook.add(Search, text="       Search      ")
notebook.add(Service, text="       Services      ")
notebook.add(THelp, text="       Help       ")

# Crear un estilo personalizado para las pestañas
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "skyblue1", "foreground": "black", "font": ("Arial", 14)},
        "map": {"background": [("selected", "Dodgerblue2")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

# Mostrar el notebook
notebook.pack(expand=True, fill=BOTH)



BFrame = ttk.Frame(ADD, padding="5 30 5 5")
BFrame.grid(column=0, row= 0)

#Frame 2

Frame2 = ttk.Frame(BFrame, padding="25 5 25 2", relief="groove")
Frame2.grid(column=0, row=0)

#Frame 3

Frame3 = ttk.Frame(Frame2, padding="10 7 35 7")
Frame3.grid(column=0, row=0, pady=10)

FName = StringVar()
LName = StringVar()
Country = StringVar()

ttk.Label(Frame3, text="First Name: ", font=("Arial", 12)).grid(column=0, row=0, sticky=(W,N), pady=1)
ttk.Label(Frame3, text="Last Name: ", font=("Arial", 12)).grid(column=2, row=0,sticky=(W,N),padx=5, pady=1)
ttk.Label(Frame3, text="", font=("Arial", 12)).grid(column=5, row=0,sticky=(W,N),padx=10, pady=1)

FirstNameEntry = ttk.Entry(Frame3, textvariable=FName, width=15, font=("Arial", 12)).grid(column=1, row=0, sticky=(W),padx=5)
LastNameEntry = ttk.Entry(Frame3, textvariable=LName, width=15, font=("Arial", 12)).grid(column=3, row=0, sticky=(W),padx=5)

#Frame 4

Frame4 = ttk.Frame(Frame2, padding="10 7 35 0")
Frame4.grid(column=0, row=1, sticky=(S))

Dia = IntVar()
Mes = StringVar()
Año = IntVar()

ttk.Label(Frame4, text="Birth Date ", font=("Arial", 12)).grid(column=0, row=0, sticky=(W,S),pady=10)
ttk.Label(Frame4, text="", font=("Arial", 12)).grid(column=5, row=0, sticky=(W,S), padx=9,pady=10)
ttk.Label(Frame4, text="Country: ", font=("Arial", 12)).grid(column=6, row=0, sticky=(W,S),pady=10)
CountryEntry = ttk.Entry(Frame4,textvariable=Country, width=10, font=("Arial", 12)).grid(column=7, row=0, sticky=(W))
ttk.Label(Frame4, text="", font=("Arial", 12)).grid(column=8, row=0, sticky=(W,S), padx=51,pady=10)


            #listas
Framelistas = ttk.Frame(Frame4)
Framelistas.grid(column=1, row=0, sticky=(S), padx=5)

DiaBox = ttk.Combobox(Framelistas, textvariable=Dia, width=2, font=("Arial", 12))
DiaBox.grid(column=0, row=0, sticky=(W,S),pady=10)
DiaBox['values'] = ("1","2","3","4","5","6","7","8",
                    "9","10","11","12","13","14","15",
                    "16","17","18","19","20","21","22",
                    "23","24","25","26","27","28","29",
                    "30","31")

MesBox = ttk.Combobox(Framelistas, textvariable=Mes, width=2, font=("Arial", 12))
MesBox.grid(column=1, row=0, sticky=(W,S), padx=2, pady=10)
MesBox['values'] = ("January","February","March","April","May","June","July","August","September",
                    "Octuber","November","December")


AñoBox = ttk.Combobox(Framelistas, textvariable=Año,width=4, font=("Arial", 12))
AñoBox.grid(column=2, row= 0,sticky=(W,S), padx=2, pady=10)
AñoBox['values'] = tuple(range(1923, 2024))

#Frame 5

Frame5 = ttk.Frame(BFrame, width=450,height=600,padding="35 2 50 2", relief="groove")
Frame5.grid(column=0, row=2, sticky=(W))

    #CreditCard

creditCard = ttk.Frame(Frame5, padding="0 0 216 0")
creditCard.grid(column=0, row=0, sticky=(W))
Credit = IntVar()

ttk.Label(creditCard, text="Credir Card (if any): ", font=("Arial", 12)).grid(column=0,row=0,sticky=(W))
CreditEntry = ttk.Entry(creditCard, textvariable=Credit, width=16, font=("Arial", 12)).grid(column=1, row=0, sticky=(W),padx=5)

    #Radio Butons

radiobu = ttk.Frame(Frame5, padding="0 20 0 0")
radiobu.grid(column=0, row=1)
ttk.Label(radiobu, text="Type Credit Card (if any): ", font=("Arial", 12)).grid(column=0, row=0,sticky=(W), pady=2)

typeCreditCard=""



                                                                               
visa = ttk.Radiobutton(radiobu, text="Visa", variable=typeCreditCard, value="Visa")
visa.grid(column=1, row=0, sticky=(W), padx=10)
masterCard = ttk.Radiobutton(radiobu, text="MasterCard", variable=typeCreditCard, value="MasterCard")
masterCard.grid(column=2, row=0,sticky=(W), padx=5)

radiobu.grid(column=0, row=3, sticky=(W))

Frame6 = ttk.Frame(BFrame,padding="50 2 50 2",width=604,height=100, relief="groove")
Frame6.grid(column=0,row=3,sticky=(W))

ttk.Label(Frame6,text="RoomType:",font=("Arial",14)).grid(column=0,row=0,sticky=(W),pady=3)

root.mainloop()