import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import airport as ap



class AirportInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Airport Management System - Version 1")
        self.root.geometry("800x550")

        self.airports = []

        # --- FRAME SUPERIOR: Botones ---
        top_frame = tk.Frame(root, pady=10)
        top_frame.pack(fill=tk.X)

        tk.Button(top_frame, text="Load Airports", command=self.load_file, width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(top_frame, text="Save Schengen", command=self.save_file, width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(top_frame, text="Plot Airports", command=self.plot_data, width=20).pack(side=tk.LEFT, padx=10)
        tk.Button(top_frame, text="Map in Google Earth", command=self.map_data, width=20).pack(side=tk.LEFT, padx=10)

        # --- FRAME CENTRAL: Tabla ---
        mid_frame = tk.Frame(root)
        mid_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columns = ("code", "lat", "lon", "schengen")
        self.tree = ttk.Treeview(mid_frame, columns=columns, show="headings")
        self.tree.heading("code", text="ICAO Code")
        self.tree.heading("lat", text="Latitude")
        self.tree.heading("lon", text="Longitude")
        self.tree.heading("schengen", text="Schengen Status")

        self.tree.column("code", anchor=tk.CENTER)
        self.tree.column("lat", anchor=tk.CENTER)
        self.tree.column("lon", anchor=tk.CENTER)
        self.tree.column("schengen", anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(mid_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # --- FRAME INFERIOR: Modificar Aeropuertos (Cambiado todo a .pack) ---
        bottom_frame = tk.LabelFrame(root, text="Modificar Lista de Aeropuertos", pady=10, padx=10)
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)

        # Fila 1: Añadir
        row1 = tk.Frame(bottom_frame)
        row1.pack(fill=tk.X, pady=5)

        tk.Label(row1, text="Code:").pack(side=tk.LEFT, padx=5)
        self.entry_code = tk.Entry(row1, width=10)
        self.entry_code.pack(side=tk.LEFT, padx=5)

        tk.Label(row1, text="Lat:").pack(side=tk.LEFT, padx=5)
        self.entry_lat = tk.Entry(row1, width=15)
        self.entry_lat.pack(side=tk.LEFT, padx=5)

        tk.Label(row1, text="Lon:").pack(side=tk.LEFT, padx=5)
        self.entry_lon = tk.Entry(row1, width=15)
        self.entry_lon.pack(side=tk.LEFT, padx=5)

        tk.Button(row1, text="Add Airport", command=self.add_airport).pack(side=tk.LEFT, padx=20)

        # Fila 2: Eliminar
        row2 = tk.Frame(bottom_frame)
        row2.pack(fill=tk.X, pady=5)

        tk.Label(row2, text="Code to Remove:").pack(side=tk.LEFT, padx=5)
        self.entry_remove = tk.Entry(row2, width=10)
        self.entry_remove.pack(side=tk.LEFT, padx=5)

        tk.Button(row2, text="Remove Airport", command=self.remove_airport).pack(side=tk.LEFT, padx=20)

    # --- MÉTODOS DE ACCIÓN (Idénticos) ---

    def load_file(self):
        filename = filedialog.askopenfilename(title="Select Airports File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if filename:
            try:
                self.airports = ap.LoadAirports(filename)
                for airport in self.airports:
                    ap.SetSchengen(airport)
                self.update_treeview()
                messagebox.showinfo("Éxito", f"Se cargaron {len(self.airports)} aeropuertos correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo.\nDetalles: {e}")

    def save_file(self):
        if not self.airports:
            messagebox.showwarning("Aviso", "La lista de aeropuertos está vacía.")
            return
        filename = filedialog.asksaveasfilename(title="Save Schengen Airports", defaultextension=".txt",
                                                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if filename:
            try:
                ap.SaveSchengenAirports(self.airports, filename)
                messagebox.showinfo("Éxito", "Los aeropuertos Schengen se guardaron correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo.\nDetalles: {e}")

    def add_airport(self):
        code = self.entry_code.get().strip().upper()
        lat_str = self.entry_lat.get().strip()
        lon_str = self.entry_lon.get().strip()

        if not code or not lat_str or not lon_str:
            messagebox.showwarning("Error de Entrada", "Por favor, rellena el Código, Latitud y Longitud.")
            return
        try:
            lat = float(lat_str)
            lon = float(lon_str)
            new_airport = ap.Airport(code, lat, lon)
            ap.SetSchengen(new_airport)
            ap.AddAirport(self.airports, new_airport)
            self.update_treeview()
            self.entry_code.delete(0, tk.END)
            self.entry_lat.delete(0, tk.END)
            self.entry_lon.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error de Entrada", "La Latitud y Longitud deben ser números decimales válidos.")

    def remove_airport(self):
        code = self.entry_remove.get().strip().upper()
        if not code:
            messagebox.showwarning("Error de Entrada", "Escribe el código del aeropuerto a eliminar.")
            return
        res = ap.RemoveAirport(self.airports, code)
        if res == -1:
            messagebox.showerror("Error", f"No se encontró ningún aeropuerto con el código {code}.")
        else:
            self.update_treeview()
            self.entry_remove.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"El aeropuerto {code} ha sido eliminado.")

    def plot_data(self):
        if not self.airports:
            messagebox.showwarning("Aviso", "No hay aeropuertos cargados para graficar.")
            return
        ap.PlotAirports(self.airports)

    def map_data(self):
        if not self.airports:
            messagebox.showwarning("Aviso", "No hay aeropuertos para mostrar en el mapa.")
            return
        ap.ShowAirportsInGoogleEarth(self.airports)
        messagebox.showinfo("Mapa", "Se ha ejecutado la función para mapear en Google Earth.")

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for a in self.airports:
            self.tree.insert("", tk.END, values=(a.ICAO, a.coordinates[0], a.coordinates[1], a.schengen))


if __name__ == "__main__":
    root = tk.Tk()
    app = AirportInterface(root)
    root.mainloop()
