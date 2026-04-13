class Airport:
    def __init__(self, ICAO, latitude, longitude):
        self.ICAO =ICAO
        self.latitude = latitude
        self.longitude = longitude
        self.schengen = False

def IsSchengenAirport(code):

    schengen_prefixes = [   'LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'ET','LG', 'EH', 'LH','BI', 'LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES', 'LS' ]
    encontrado=False
    prefix=str(code[0:2])

    for i in  schengen_prefixes:
        if prefix==i:
            encontrado = True
        if prefix=="":
            encontrado = False

    return encontrado

def SetSchengen(airport):
    airport.schengen = IsSchengenAirport(airport.ICAO)

def PrintAirport (airport):
    print(f"ICAO: {airport.ICAO}")
    print(f"Coordinates: {airport.latitude}, {airport.longitude}")
    print(f"Schengen: {airport.schengen}")


def LoadAirports(filename):
    airports = []
    try:
        f=open(filename, 'r')

        lines = f.readlines()

        for line in lines[1:]:
             parts = line.strip().split()
             if len(parts) == 3:

                code = parts[0]
                # Convert DMS string (e.g., N635906) to decimal
                lat_str = parts[1]
                lat = int(lat_str[1:3]) + int(lat_str[3:5]) / 60 + int(lat_str[5:7]) / 3600
                if lat_str[0] == 'S':
                    lat = -lat

                lon_str = parts[2]
                lon = int(lon_str[1:4]) + int(lon_str[4:6]) / 60 + int(lon_str[6:8]) / 3600
                if lon_str[0] == 'W':
                    lon = -lon

                airports.append(Airport(code, lat, lon))
    except FileNotFoundError:
        return []
    return airports


def SaveSchengenAirports(airports, filename):

    if len(airports) == 0:
        return " Error, no hay nafda"

    f = open(filename, 'w')
    f.write("CODE LAT LON")

    for a in airports:
        if a.schengen == True:
            linea = a.ICAO + " " + str(a.latitude) + " " + str(a.longitude) + "\n"
            f.write(linea)
    return 0


def AddAirport(airports, airport):


    encontrado = False
    i = 0
    num_airports = len(airports)


    while i < num_airports and not encontrado:
        if airports[i].ICAO == airport.ICAO:
            encontrado = True
        i = i + 1

    # 3. Conditional Statement: Solo añadimos si NO se encontró
    if encontrado == False:
        airports.append(airport)


def RemoveAirport(airports, code):
    encontrado = False
    i = 0
    n = len(airports)


    while i < n and not encontrado:
        if airports[i].ICAO == code:
            encontrado = True
        else:
            i = i + 1


    if encontrado:

        while i < n-1:
            airports[i]=airports[i+1]
            i=i+1
    aeros=[]
    for j in range(n-1):
        aeros.append(airports[j])
    airports=aeros
    return 0


import matplotlib.pyplot as plt


def PlotAirports(airports):

    n_schengen = 0
    n_no_schengen = 0

    for a in airports:
        if a.schengen == True:
            n_schengen = n_schengen + 1
        else:
            n_no_schengen = n_no_schengen + 1



    labels = ['Airports']


    plt.figure()


    plt.bar(labels, [n_schengen], label='Schengen', color='steelblue')


    plt.bar(labels, [n_no_schengen], bottom=[n_schengen], label='No Schengen', color='lightcoral')


    plt.ylabel('Count')
    plt.title('Schengen airports')
    plt.legend()


    plt.show()


def MapAirports(airports, filename="airports.kml"):

    f = open(filename, 'w')


    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    f.write('<Document>\n')
    f.write('  <name>Airports Map</name>\n')


    for a in airports:


        if a.schengen == True:
            color = "ff0000ff"
        else:
            color = "ffff0000"

      
        f.write('  <Placemark>\n')
        f.write('    <name>' + a.ICAO + '</name>\n')
        f.write('    <Style>\n')
        f.write('      <IconStyle>\n')
        f.write('        <color>' + color + '</color>\n')
        f.write('      </IconStyle>\n')
        f.write('    </Style>\n')
        f.write('    <Point>\n')

        f.write('      <coordinates>' + str(a.longitude) + ',' + str(a.latitude) + ',0</coordinates>\n')
        f.write('    </Point>\n')
        f.write('  </Placemark>\n')


    f.write('</Document>\n')
    f.write('</kml>\n')
    f.close()
    print(f"Archivo {filename} generado. Ábrelo con Google Earth.")
