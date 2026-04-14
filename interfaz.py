from tkinter import *
import airport as ap

airports = []

def Load():
    airports.clear()
    airports.extend(ap.LoadAirports(pathEntry.get()))
    for a in airports:
        ap.SetSchengen(a)

def Add():
    new = ap.Airport(ICAOEntry.get(), 0, 0)
    ap.SetSchengen(new)
    ap.AddAirport(airports, new)

def Remove():
    ap.RemoveAirport(airports, ICAOEntry.get())

def plot():
    if not airports:
        print("Carga aeropuertos")
    ap.PlotAirports(airports)

def Map():
    if airports:
        ap.MapAirports(airports, "airports.kml")

# Finestra
window = Tk()
window.title("Airport")
window.geometry("500x350")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)

#Títols
tituloLabel = Label(window, text="Airport Manager", font=("Courier", 18, "bold"))
tituloLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)

#Arxius
archivoLabel = Label(window, text="Archivo:")
archivoLabel.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

pathEntry = Entry(window)
pathEntry.insert(0, "Airports.txt")
pathEntry.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+E+W)

# Pel que fa ICAO:
ICAOLabel = Label(window, text="ICAO:")
ICAOLabel.grid(row=2, column=0, padx=5, pady=5, sticky=N+S+E+W)

ICAOEntry = Entry(window)
ICAOEntry.grid(row=2, column=1, padx=5, pady=5, sticky=N+S+E+W)

#Botons
Button(window, text="Load Airports", bg="blue", fg="white", command=Load).grid(row=3, column=0, columnspan=2, padx=5, pady=3, sticky=N+S+E+W)
Button(window, text="Add Airport",   bg="green", fg="white", command=Add).grid(row=4, column=0, columnspan=2, padx=5, pady=3, sticky=N+S+E+W)
Button(window, text="Remove Airport",bg="red",   fg="white", command=Remove).grid(row=5, column=0, columnspan=2, padx=5, pady=3, sticky=N+S+E+W)
Button(window, text="Ver Gráfico",   bg="orange",            command=plot).grid(row=6, column=0, padx=5, pady=3, sticky=N+S+E+W)
Button(window, text="Google Earth",  bg="orange",            command=Map).grid(row=6, column=1, padx=5, pady=3, sticky=N+S+E+W)

window.mainloop()