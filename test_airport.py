from airport import *
airport = Airport ("LEBL", 41.297445, 2.0832941)
SetSchengen(airport)
PrintAirport (airport)

airport_list = LoadAirports("Airports.txt")
print(f"Loaded {len(airport_list)} airports.")

for a in airport_list:
    SetSchengen(a)
new_ap = Airport("PRUEBA", 0.0, 0.0)
AddAirport(airport_list, new_ap)
print(f"List size after adding PRUEBA: {len(airport_list)}")

RemoveAirport(airport_list, "PRUEBA")
print(f"List size after removing PRUEBA: {len(airport_list)}")


result = SaveSchengenAirports(airport_list, "Schengen_Airports.txt")
if result == 0:
    print("Successfully saved Schengen airports to file.")
PlotAirports(airport_list)


# En test_airports.py, al final:
from airport import MapAirports

print("\n--- TEST: MapAirports (Google Earth) ---")


MapAirports(airport_list, "Mapa_Aeropuertos.kml")

print("Busca el archivo 'Mapa_Aeropuertos.kml' en tu carpeta y ábrelo con Google Earth.")
