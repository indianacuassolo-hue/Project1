from airport import *


print("-Check step 1-")

airport = Airport("LEBL", 41.297445, 2.0832941)
SetSchengen(airport)
PrintAirport(airport)


print("-Check step 3-")

airport_list = LoadAirports("Airports.txt")
print(f"Loaded {len(airport_list)} airports.")


for ap in airport_list:
    SetSchengen(ap)


new_ap = Airport("PRUEBA", 0.0, 0.0)
AddAirport(airport_list, new_ap)
print(f"List size after adding PRUEBA: {len(airport_list)}")


RemoveAirport(airport_list, "PRUEBA")
print(f"List size after removing PRUEBA: {len(airport_list)}")


result = SaveSchengenAirports(airport_list, "Schengen_Airports.txt")
if result == 0:
    print("Successfully saved Schengen airports to file.")

PlotAirports(airport_list)
# ... (todo tu código anterior de check step 3) ...

# --- NUEVO: Check Google Earth ---
print("-Check Google Earth-")
ShowAirportsInGoogleEarth(airport_list, "Airports_Map.kml")

# Finalmente el plot (que pausa la ejecución hasta que cierres la ventana)
PlotAirports(airport_list)
